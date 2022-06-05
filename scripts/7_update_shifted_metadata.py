import json
import os
import numpy as np
import random

mp4_cid = "QmSd9kME3zG2GnTbsBeL6XvtCynJPxbJbkW758S5jXYFhN"

image_cid = "QmS8T7GJCD47sHRrrM9TcimgUfrxvyTQ2BBseWXv2c1mDZ"

image_t_cid = "QmS8T7GJCD47sHRrrM9TcimgUfrxvyTQ2BBseWXv2c1mDZ"

pfp_cid = "QmS8T7GJCD47sHRrrM9TcimgUfrxvyTQ2BBseWXv2c1mDZ"

pfp_t_cid = "QmS8T7GJCD47sHRrrM9TcimgUfrxvyTQ2BBseWXv2c1mDZ"

apng_cid = "QmS8T7GJCD47sHRrrM9TcimgUfrxvyTQ2BBseWXv2c1mDZ"

gif_cid = "QmS8T7GJCD47sHRrrM9TcimgUfrxvyTQ2BBseWXv2c1mDZ"

os.makedirs("/Users/chrisrussell/Cryptids/cryptid-generation/output/shifted/metadata_final", exist_ok=True)



def main():
    names = json.load(open("/Users/chrisrussell/Cryptids/cryptid-generation/scripts/names2.json"))

        
    name_file = open("/Users/chrisrussell/Cryptids/cryptid-generation/deep_names.txt", "r")
    data = name_file.read()
    name_list = data.split("\n")
    name_file.close()

    


    for filename in os.scandir("/Users/chrisrussell/Cryptids/cryptid-generation/output/shifted/metadata"):
        name = name_list.pop(random.randrange(len(name_list)))
        if len(filename.name.split(".")) != 2:
            continue
        file_name = filename.name.split(".")[0]
        transformed = transform_json(json.load(open(filename.path)), names, file_name, name)

        with open(f"/Users/chrisrussell/Cryptids/cryptid-generation/output/shifted/metadata_final/{file_name}.json", "w") as o:
            json.dump(transformed, o, indent=4)
    print('Success!')

def transform_json(data, names, file_name, cryptid_name):
    # print(file_name)
    metadata = {
        "name": f"{cryptid_name}",
        "description": "Part fantasy, part science-fiction. Cryptids is a generative art collection of 7,777 fantastic mythical creatures.",
        "image": f"ipfs://{image_cid}/{file_name}.png",
        "animation_url": f"ipfs://{mp4_cid}/{file_name}.mp4",
        "pfp": f"ipfs://{pfp_cid}/{file_name}.png",
        "pfp_t": f"ipfs://{pfp_t_cid}/{file_name}.png",
        "image_t": f"ipfs://{image_t_cid}/{file_name}.png",
        "apng": f"ipfs://{apng_cid}/{file_name}.png",
        "gif": f"ipfs://{gif_cid}/{file_name}.png",
        
  
    
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

    # metadata["attributes"].append(
    #         {"display_type": "boost_number", "trait_type": "Magic", "value": magic}
    #     )
    # metadata["attributes"].append(
    #         {"display_type": "boost_number", "trait_type": "Empathy", "value": empathy}
    #     )
    # metadata["attributes"].append(
    #         {"display_type": "boost_number", "trait_type": "Morality", "value": morality}
    #     )
    # metadata["attributes"].append(
    #         {"display_type": "boost_number", "trait_type": "Wisdom", "value": wisdom}
    #     )
    # metadata["attributes"].append(
    #         {"display_type": "boost_number", "trait_type": "Chaos", "value": chaos}
    #     )

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
    # metadata["attributes"].append(
    #         {"display_type": "number", "trait_type": "Generation", "value": 1}
    #     )

    return metadata

if __name__ == "__main__":
    main()

