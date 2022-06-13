import os
from pathlib import Path
from re import L 
import ipfshttpclient
import fnmatch
from pinatapy import PinataPy


files = {"_solid.png": "image", "_solid_pfp.png": "pfp", ".mp4": "mp4", "_transparent.png": "image_t", "_transparent_pfp.png": "pfp_t", "_apng.png": "apng", ".gif":"gif"}


for file in files:
    image_path = f"/Users/chrisrussell/Cryptids/cryptid-generation/output/shifted/{files[file]}"
    image_list = fnmatch.filter(os.listdir(image_path), f'*{file}')
    image_count = len(image_list)

    client = ipfshttpclient.connect()

    response = client.add(image_path, wrap_with_directory=False, pattern=f'*{file}')
    ipfs_hash_directory = response[image_count]['Hash']

    base_url = 'https://ipfs.io/ipfs/'
    final_url = base_url + ipfs_hash_directory
    print(f"IPFS {files[file]} directory CID is: {ipfs_hash_directory}\n")
    print(f" \nGo to folder: {final_url}\n")
    with open('hash_pins.txt', 'a') as f:
        f.write(f" \nIPFS {files[file]} directory CID is: {ipfs_hash_directory}\n")
        f.write(f" \nGo to folder: {final_url}\n")
        f.close

    # api_key = os.environ.get("PINATA_API_KEY")
    # secret_key = os.environ.get("PINATA_SECRET_API_KEY")
    # if api_key and secret_key:
    #     pinata = PinataPy(api_key, secret_key)
    # else:
    #     raise ValueError("No API keys in environment variables")

    # response = pinata.pin_hash_to_ipfs(ipfs_hash_directory, f'{files[file]}')

    print(response)
