import json
import os
import operator

def get_max(dicts):
    return max(list(dicts.values()))

def count_files(dir):
    return len([1 for x in list(os.scandir(dir)) if x.is_file()])

def main():

    
    names = json.load(open("/Users/chrisrussell/CryptidToken/generation/names2.json"))
    metadata = {}

    metadata_dir = "/Users/chrisrussell/CryptidToken/generation/output/metadata"
    file_count = count_files(metadata_dir)
    

    for filename in os.scandir(metadata_dir):
        if len(filename.name.split(".")) != 2:
            continue
        
        data = json.load(open(filename.path))

        for x in data.items():

            if x[1] in names.keys():
            
                combined = str(names[x[0]]+ ', ' + names[x[1]])

                if combined in metadata:
                    metadata[combined] += 1
                else:
                    metadata[combined] = 1

    new = {k: v for k, v in sorted(metadata.items(), key=lambda item: item[1], reverse=True)}

    with open("/Users/chrisrussell/CryptidToken/generation/rarity.json", "w") as w:
        json.dump(new, w, indent=4)

    print('Success!')

if __name__ == "__main__":
    main()