import json
import os
import numpy as np

gif_cid = "QmV7d7KaXmxTfxFd9PdgtJpLVLwjyjeDgFnnGWoj79f5D3" 
mp4_cid = "QmaChPE8uobvscmKDjNwarzzWki2F2WHvK3raiXPqGF71V"
image_cid = "QmcSNSXTwUU7S3nG5C65Kr48RnHYjSpReUU1KZsCLsqv4S"
still_image_cid = "QmczDCw4Rnuyb54WXMgTAVrFUermxHuMCwZFGhGam6WKZX"
still_image_t_cid = "QmaJa49QZ65AUhKJ5tujq5jSan2hDcZnAuhuvCk3sJozVj"

pfp_cid = "Qme8escZxhsLonXKTH361zeJEbRL3rBPcwNp9npqkVEZQa"
pfp_t_cid = "QmRnjSWGQzvPJaLSNM8stRSa37t3gdtrzmtpocfveWhrSs"



os.makedirs("/Users/chrisrussell/Cryptids/cryptid-generation/output/shifted/metadata_final", exist_ok=True)

def main():
    names = json.load(open("/Users/chrisrussell/Cryptids/cryptid-generation/scripts/names.json"))

        
    name_file = open("/Users/chrisrussell/Cryptids/cryptid-generation/deep_names_shuffle_shifted.txt", "r")
    data = name_file.read()
    name_list = data.split("\n")
    name_file.close()


    # for filename in os.scandir("/Users/chrisrussell/Cryptids/cryptid-generation/output/shifted/metadata"):

    for file_name in range(1,7778):
        name = name_list.pop(0)
        # if len(filename.name.split(".")) != 2:
        #     continue
        # file_name = filename.name.split(".")[0]
        transformed = transform_json(json.load(open(f'/Users/chrisrussell/Cryptids/cryptid-generation/output/shifted/metadata/{file_name}.json')), names, file_name, name)

        with open(f"/Users/chrisrussell/Cryptids/cryptid-generation/output/shifted/metadata_final/{file_name}.json", "w") as o:
            json.dump(transformed, o, indent=4)
    print('Success!')

def transform_json(data, names, file_name, cryptid_name):
    # print(file_name)
    metadata = {
        "name": f"{cryptid_name}",
        "description": "Mythical chimeras rule over domains in a foreign universe. From the shadows of Nos Atomos lurk its original inhabitants, the CRYPTIDS. They will defend, conquer, or aid you in this new land. Only 7,777 await your discovery. A generative art collection created by @no__solo and @chrisrusselljr.",
        "image": f"http://52.8.140.24/ipfs/{gif_cid}/{file_name}.gif",
        "animation_url": f"http://52.8.140.24/ipfs/{mp4_cid}/{file_name}.mp4",
        "still_image": f"http://52.8.140.24/ipfs/{still_image_cid}/{file_name}_solid.png",
        "still_image_t": f"http://52.8.140.24/ipfs/{still_image_t_cid}/{file_name}_transparent.png",
        "pfp": f"http://52.8.140.24/ipfs/{pfp_cid}/{file_name}_solid_pfp.png",
        "pfp_t": f"http://52.8.140.24/ipfs/{pfp_t_cid}/{file_name}_transparent_pfp.png",
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
 

    # split mane and wing types
    if "7_fur" in data:
        _, fur_type, fur_color = data['7_fur'].split('_')
        metadata["attributes"].append({"trait_type": "Mane Type", "value": fur_type.capitalize()})
        metadata["attributes"].append({"trait_type": "Mane Color", "value": fur_color.capitalize()})

    if "4_back" in data:
        _, back_type, back_color = data['4_back'].split('_')
        metadata["attributes"].append({"trait_type": "Back Type", "value": back_type.capitalize()})
        metadata["attributes"].append({"trait_type": "Back Color", "value": back_color.capitalize()})
           
    for x in data.items():
        # print(x)
        # print(x[1])
        # print(names.values())
        if x[1] in names.keys():
            # print(x[1])
            # print(names.values())
           
            # For each sub-item in attribute
        
            metadata["attributes"].append({"trait_type": names[x[0]], "value": names[x[1]]})
   
    # Boost attributes
    magic = np.random.randint(1,11)
    empathy = np.random.randint(1,11)
    morality = np.random.randint(1,11)
    wisdom = np.random.randint(1,11)
    chaos = np.random.randint(1,11)

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

