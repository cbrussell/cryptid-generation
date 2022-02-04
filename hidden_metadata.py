import json
import os
import os
from pathlib import Path 
import ipfshttpclient
from pinatapy import PinataPy

dir_path = os.path.dirname(os.path.realpath(__file__))
# default_image_cid = "QmcAVC3xkYTR2ZyDwW7rkKDQHwQy8C5W5bsKzwKa1zrNh3"

def upload_default_image():
    image_path = f"{dir_path}/assets/default_image/loading.png"

    client = ipfshttpclient.connect()

    response = client.add(image_path, wrap_with_directory=False, pattern='*.png')
    print(response)
    ipfs_hash_directory = response['Hash']

    base_url = 'https://ipfs.io/ipfs/'
    final_url = base_url + ipfs_hash_directory
    
    print(f" \nIPFS image directory CID is: {ipfs_hash_directory}\n")
    print(f" \nGo to folder: {final_url}\n")
    

    api_key = os.environ.get("PINATA_API_KEY")
    secret_key = os.environ.get("PINATA_SECRET_API_KEY")
    if api_key and secret_key:
        pinata = PinataPy(api_key, secret_key)
    else:
        raise ValueError("No API keys in environment variables")

    response = pinata.pin_hash_to_ipfs(ipfs_hash_directory, "Prereveal Images")

    return ipfs_hash_directory

def main():

    default_image_cid = upload_default_image()
    metadata = {
        
        "name": "Cyptids",
        "description": "The administrators of the metaverse.",
        "image": f"ipfs://{default_image_cid}",

    }
    with open(f"{dir_path}/hidden.json", "w") as f:
        json.dump(metadata, f, indent=4)

    print("Success!")


# IPFS Daemon must be running

# Function will upload image directory to IPFS then pin file to Pinata

def upload_to_ipfs():
    image_path = f"{dir_path}/hidden.json"
    client = ipfshttpclient.connect()

    response = client.add(image_path)
    print(response)
    ipfs_hash_directory = response['Hash']

    base_url = 'https://ipfs.io/ipfs/'
    final_url = base_url + ipfs_hash_directory
    default_uri = 'ipfs://' + ipfs_hash_directory

    print(f" \nIPFS image directory CID is: {ipfs_hash_directory}\n")
    print(f" \nGo to folder: {final_url}\n")
    print(f" \nFOR CONTRACT: Default URI is: {default_uri}\n")
    
    api_key = os.environ.get("PINATA_API_KEY")
    secret_key = os.environ.get("PINATA_SECRET_API_KEY")
    if api_key and secret_key:
        pinata = PinataPy(api_key, secret_key)
    else:
        raise ValueError("No API keys in environment variables")

    response = pinata.pin_hash_to_ipfs(ipfs_hash_directory, "Prereveal Metadata")

    print(response)

if __name__ == "__main__":
    main()
    upload_to_ipfs()