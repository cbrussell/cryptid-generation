import os
import json
from datetime import datetime
from multiprocessing import Process, Manager, Value
from dna import get_dna, to_hash
from traits import TraitManifest, ColorManifest, BackgroundManifest
# from combine import combine_attributes
# from combine_transparent import combine_attributes
# from combine_solid_transparent import combine_attributes
from combine_transparent_accent import combine_attributes

def main():
    open('colors.txt', 'w').close()
    dir_path = os.path.dirname(os.path.realpath(__file__))

    trait_manifest = TraitManifest(json.load(open(f'{dir_path}/trait_manifest.json')))
    color_manifest = ColorManifest(json.load(open(f'{dir_path}/color_manifest.json')))
    background_manifest = BackgroundManifest(json.load(open(f'{dir_path}/background_manifest_solid.json')))
    os.makedirs(f"{dir_path}/output/stills", exist_ok=True)
    os.makedirs(f"{dir_path}/output/bg", exist_ok=True)

    start_time = datetime.now()
    procs = 1
    n = 100 # collection size
    increment = int(n / procs)
    jobs = []
    start = 1
    stop = increment + 1

    with Manager() as manager:
        hashlist = manager.list()
        duplicates = manager.Value('duplicates', 0)
        size = manager.Value('size', n)
        for i in range(0, procs):
            process = Process(target=worker, args=(start, stop, hashlist, duplicates, trait_manifest, color_manifest, background_manifest, size))
            start = stop
            stop += increment
            jobs.append(process)

        [j.start() for j in jobs]
        [j.join() for j in jobs]

        end_time = datetime.now()
        elapsed_time = end_time - start_time
        collection_total = (len(hashlist))
        print(f'{collection_total} of {n} cryptids generated in {elapsed_time}. {duplicates.value} duplicates found.')
     
    return

def worker(start: int, stop: int, hashlist: list, duplicates: int, trait_manifest: TraitManifest, color_manifest: ColorManifest, background_manifest: BackgroundManifest, size: int):
    number = 0
    unique_dna_tolerance = 100000
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    for edition in range(start, stop):
       
        
        images, dna  = get_dna(trait_manifest, color_manifest, background_manifest)
        hashed_dna = to_hash(dna)   
        
        while duplicates.value < unique_dna_tolerance:
            if hashed_dna not in hashlist:
                hashlist.append(hashed_dna)
                break
            else:
                duplicates.value += 1
                images, dna  = get_dna()
                hashed_dna = to_hash(dna)
                print(f'Duplicate DNA found... {duplicates.value}/{unique_dna_tolerance}')   
        if duplicates.value >= unique_dna_tolerance:
            print('Found {duplicates.values} duplicates (MAX). Tolerance is set to {unique_dna_tolerance}.')
            return
        else:
            print(f'Building edition #{edition}/{stop - 1}')
            os.makedirs(f"{dir_path}/output/raw/{str(edition)}", exist_ok=True)
            os.makedirs(f"{dir_path}/output/metadata", exist_ok=True)
            with open(f"{dir_path}/output/metadata/{str(edition)}.json", "w") as f:
                json.dump(dna, f, indent=4)
                combine_attributes(images, str(edition))
                number += 1
                print(f"Completed edition #{edition}/{stop - 1}")

 
    print(f'Multiprocess job complete! For process ID {os.getpid()}, {number} generated. Found {duplicates.value} duplicates.')

if __name__ == "__main__":
    main()

