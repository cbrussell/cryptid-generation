import json
import os
import numpy as np
import random


image_cid = "QmZ1JpvWzpEZNVYYVgRe2X6AAMBbWLb2yAF1RJp4LeUvez"

pfp_cid = "QmWyincg4PWhoN4vufoG37LAEw654Aq32ThKCYsteJ2xjk"

mp4_cid = "QmNnGUUHJFD8YnDD8cj6yD5wfdC23V8r8th1S9Bb3s3ti5"


os.makedirs("/Users/chrisrussell/Cryptids/cryptid-generation/output/shifted/metadata_final", exist_ok=True)



def main():
    names = json.load(open("/Users/chrisrussell/Cryptids/cryptid-generation/scripts/names.json"))

        
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
        "description": "Part fantasy, part science-fiction. Cryptids is a generative art collection of 7,777 fantastic mythical creatures. Art by @no__solo.",
        "image": f"ipfs://{image_cid}/{file_name}_solid.png",
        "animation_url": f"ipfs://{mp4_cid}/{file_name}.mp4",
        "pfp": f"ipfs://{pfp_cid}/{file_name}_solid_pfp.png",
        "attributes": []

    }

# iris = color
# pupil = type

    # "eyes_scar_left": "Scar",
    # "eyes_scar_right": "Scar",
 
    
    for x in data.items():
        if x == ("eyes_scar_left", "Scar"):
            # data["14e_eyes_iris_right"]
            data["14b_eyes_iris_left"] = data["14e_eyes_iris_right"].replace('right', 'left')
            data["14c_eyes_pupil_left"] = data["14f_eyes_pupil_right"].replace('right', 'left')

            
    # "14c_eyes_pupil_left": "eyes_wise_pupil_left",

    #             "14e_eyes_iris_right": "eyes_wise_iris_right_brown",
    # "14f_eyes_pupil_right": "eyes_wise_pupil_right",
    #         data.pop("14b_eyes_iris_left")


    #         data.pop("14e_eyes_iris_right")

    remove = [k for k in data.items() if k == ("eye_special", "multi")]
    for k in remove: 
        del data["14b_eyes_iris_left"]
        del data["14e_eyes_iris_right"]

    # for x in data.items():
    #     if x == ("eye_special", "multi"):
    #         del data["14b_eyes_iris_left"]
    #         del data["14e_eyes_iris_right"
 
                   

    for x in data.items():
        print(x)
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

