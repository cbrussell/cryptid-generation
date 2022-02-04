import json
import os
import numpy as np

mp4_cid = "QmXkFbUZUNqNUk7G2c4VNBAV6Ty6jpwuphc6oJADjFHdhr"
still_cid = "QmS8T7GJCD47sHRrrM9TcimgUfrxvyTQ2BBseWXv2c1mDZ"

def main():
    names = json.load(open("/Users/chrisrussell/CryptidToken/generation/names2.json"))
    for filename in os.scandir("/Users/chrisrussell/CryptidToken/generation/output/metadata_shifted"):
        if len(filename.name.split(".")) != 2:
            continue
        file_name = filename.name.split(".")[0]
        transformed = transform_json(
            json.load(open(filename.path)), names, file_name
        )

        with open(f"/Users/chrisrussell/CryptidToken/generation/output/metadata_shifted_final/{file_name}.json", "w") as o:
            json.dump(transformed, o, indent=4)
    print('Success!')

def transform_json(data, names, file_name):
    # print(file_name)
    metadata = {
        "name": f"Cyptid #{file_name}",
        "description": "",
        "image": f"ipfs://{still_cid}/{file_name}.png",
        "animation_url": f"ipfs://{mp4_cid}/{file_name}.mp4",
        "attributes": []

    }
    for x in data.items():
        # print(x)
        print(x[1])
        print(names.values())
        if x[1] in names.keys():
            print(x[1])
            print(names.values())
           
            # For each sub-item in attribute
        
            metadata["attributes"].append({"trait_type": names[x[0]], "value": names[x[1]]})
   
    # Boost attributes
    magic = np.random.randint(50,100)
    empathy = np.random.randint(50,100)
    morality = np.random.randint(50,100)
    wisdom = np.random.randint(50,100)
    chaos = np.random.randint(50,100)

    metadata["attributes"].append(
            {"display_type": "boost_number", "trait_type": "Magic", "value": magic}
        )
    metadata["attributes"].append(
            {"display_type": "boost_number", "trait_type": "Empathy", "value": empathy}
        )
    metadata["attributes"].append(
            {"display_type": "boost_number", "trait_type": "Morality", "value": morality}
        )
    metadata["attributes"].append(
            {"display_type": "boost_number", "trait_type": "Wisdom", "value": wisdom}
        )
    metadata["attributes"].append(
            {"display_type": "boost_number", "trait_type": "Chaos", "value": chaos}
        )

    metadata["attributes"].append(
            {"trait_type": "Magic", "value": magic}
        )
    metadata["attributes"].append(
            {"trait_type": "Empathy", "value": empathy}
        )
    metadata["attributes"].append(
            {"trait_type": "Morality", "value": morality}
        )
    metadata["attributes"].append(
            {"trait_type": "Wisdom", "value": wisdom}
        )
    metadata["attributes"].append(
            {"trait_type": "Chaos", "value": chaos}
        )
    metadata["attributes"].append(
            {"display_type": "number", "trait_type": "Generation", "value": 1}
        )

    return metadata

if __name__ == "__main__":
    main()

