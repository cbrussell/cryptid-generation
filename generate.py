import os
import json
from datetime import datetime
from multiprocessing import Process, Manager, Value
from dna import get_dna, to_hash
from traits import TraitManifest, ColorManifest, BackgroundManifest
from combine import combine_attributes

def main():

    if os.path.exists("iris_colors.txt"):
        os.remove("iris_colors.txt")

    dir_path = os.path.dirname(os.path.realpath(__file__))
    trait_manifest = TraitManifest(json.load(open(f'{dir_path}/trait_manifest.json')))
    color_manifest = ColorManifest(json.load(open(f'{dir_path}/color_manifest.json')))
    background_manifest = BackgroundManifest(json.load(open(f'{dir_path}/background_manifest.json')))
    os.makedirs(f"{dir_path}/output/stills", exist_ok=True)
    start_time = datetime.now()



    with Manager() as manager:
        if os.path.exists("hash_list.txt"):
            hash_list = [line.strip() for line in open('hash_list.txt')]
            hashlist = manager.list(hash_list)
        else:
            hashlist = manager.list()

        beginning_index = len(hashlist)


        procs = 10  # number of processors
        n = 2000 # collection size
        frame_count = 72 # 1 for stills, 72 for animation

        increment = int(n / procs)
        jobs = []
        start = beginning_index + 1
        stop = beginning_index + 1 + increment

        duplicates = manager.Value('duplicates', 0) 
        size = manager.Value('size', n)
        for i in range(0, procs):
            process = Process(target=worker, args=(start, stop, hashlist, duplicates, trait_manifest, color_manifest, background_manifest, size, frame_count))
            start = stop
            stop += increment
            jobs.append(process)

        [j.start() for j in jobs]
        [j.join() for j in jobs]

        end_time = datetime.now()
        elapsed_time = end_time - start_time
        collection_total = len(hashlist)
        with open('hash_list.txt', 'w') as f:
            for item in hashlist:
                f.write("%s\n" % item)
        
        newly_created = collection_total - beginning_index
        print(f'{newly_created} of {n} cryptids generated in {elapsed_time}. Total number of cryptids generated is now {collection_total}. {duplicates.value} duplicates found.')
     
    return

def worker(start: int, stop: int, hashlist: list, duplicates: int, trait_manifest: TraitManifest, color_manifest: ColorManifest, background_manifest: BackgroundManifest, size: int, frame_count: int):
    number = 0
    unique_dna_tolerance = 100000
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    for edition in range(start, stop):
       
        
        images, dna  = get_dna(trait_manifest, color_manifest, background_manifest)
        base_color_pop = dna.pop('base_color')

        hashed_dna = to_hash(dna)   
        dna['base_color'] = base_color_pop
        
        while duplicates.value < unique_dna_tolerance:
            if hashed_dna not in hashlist:
                hashlist.append(hashed_dna)

                break
            else:
                duplicates.value += 1
                images, dna  = get_dna()
                base_color_pop = dna.pop('base_color')
                hashed_dna = to_hash(dna)
                dna['base_color'] = base_color_pop
                print(f'Duplicate DNA found... {duplicates.value}/{unique_dna_tolerance}')   
        if duplicates.value >= unique_dna_tolerance:
            print('Found {duplicates.values} duplicates (MAX). Tolerance is set to {unique_dna_tolerance}.')
            return
        else:
            print(f'Building edition #{edition}/{stop - 1}')
            os.makedirs(f"{dir_path}/output/raw/{str(edition)}", exist_ok=True)
            # os.makedirs(f"{dir_path}/output/metadata", exist_ok=True)
            with open(f"{dir_path}/output/stills/{str(edition)}.json", "w") as f:
                json.dump(dna, f, indent=4)
                combine_attributes(images, str(edition), frame_count)
                number += 1
                print(f"Completed edition #{edition}/{stop - 1}")

    print(f'Multiprocess job complete! For process ID {os.getpid()}, {number} generated. Found {duplicates.value} duplicates.')

if __name__ == "__main__":
    main()