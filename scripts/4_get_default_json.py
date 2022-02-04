import os
from pathlib import Path 
import ipfshttpclient
import fnmatch
from pinatapy import PinataPy

# IPFS Daemon must be running

# Function will upload image directory to IPFS then pin file to Pinata

image_path = Path(__file__).resolve().parents[1] / "assets/default_image/loading.png"
# image_list = fnmatch.filter(os.listdir(image_path), '*.png')
# image_count = len(image_list)

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

print(response)