import os
import ipfshttpclient
import fnmatch
from pinatapy import PinataPy

# IPFS Daemon must be running

json_path = "/Users/chrisrussell/Cryptids/cryptid-generation/output/shifted/metadata_final/"
json_list = fnmatch.filter(os.listdir(json_path), '*.json')
json_count = len(json_list)

client = ipfshttpclient.connect()

response = client.add(json_path, wrap_with_directory=False, pattern='*.json')
ipfs_hash_directory = response[json_count]['Hash']

base_url = 'https://ipfs.io/ipfs/'
final_url = base_url + ipfs_hash_directory
print(f" \nIPFS json directory CID is: {ipfs_hash_directory}/\n")
print(f" \nGo to folder: {final_url}\n")

base_uri = 'ipfs://' + ipfs_hash_directory
print(f" \nBase URI for contract is: {base_uri}\n")

# api_key = os.environ.get("PINATA_API_KEY")
# secret_key = os.environ.get("PINATA_SECRET_API_KEY")
# if api_key and secret_key:
#     pinata = PinataPy(api_key, secret_key)
# else:
#     raise ValueError("No API keys in environment variables")

# response = pinata.pin_hash_to_ipfs(ipfs_hash_directory, "Final JSONs")

# print(response)