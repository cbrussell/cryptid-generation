import os
from pathlib import Path 
import fnmatch
import json

# Replaces exisitng CID in metadata - no number changes.

base_url = "ipfs://"

# Set new CID here from Step 2
new_image_cid = "QmRWxQhDAGNYMcmryvvuw1ewD9xeZU9E12ytp8ysDpFo9k/"
image_extension = ".png"

# Determine image path
json_path = Path(__file__).resolve().parents[2] / "assets/shifted_json/"

# sort directory of json files
json_list = fnmatch.filter(os.listdir(json_path), '*.json')
sorted_json_list = sorted(json_list, key=lambda x: int(os.path.splitext(x)[0]))
json_count = len(sorted_json_list)
print(sorted_json_list)

# iterate through sorted list, replace metadata with new image data, using json file name
for i in range(json_count):

    # open stream of json file for reading
    jsonFile =  open(Path(json_path /sorted_json_list[i]), "r")

    #return json object from file
    json_object = json.load(jsonFile)

    # close file-reading stream
    jsonFile.close()

    old_image = json_object["image"]

    print(f"Old image URI is: {old_image}.")
    # assign new image CID to json_object
    json_object["image"] = base_url + new_image_cid + str(i+1) + image_extension

    new_image = json_object["image"]
    print(f"New image URI is: {new_image}.")
    # open a stream of file for writing
    jsonFile = open(Path(json_path /sorted_json_list[i]), "w") 

    # call json dump with json_object as the data being stored
    json.dump(json_object, jsonFile, indent = 2)

    # close file writing stream
    jsonFile.close()
        
