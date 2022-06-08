import os
from pinatapy import PinataPy



cids = ['QmZEJVfd3FoNWhYTcpxyBWyhs2cViubfpWJpGqUT1BCjWG', 'QmRTHPqhC1xYhTbFXsL3fW5DZo1qKuCTpKoejX8HWcgtAw', 'QmVVMD3yRB4u8qjof23eJDZ4AtEgdCV7qJ6u3BSum4ebJy'
, 'QmTmMrqtG1xvj2eegSt9PJds7xUMB5UhKbPLQW2aSniz8t', 'QmPmYFFMktepfvfhnWBz6o9FeicDoGTwexBy6wqrVRvP7v', 'QmXiWUDwtFdmF7gdwhb8uXy4r1gRmZj7Y5EzjjNiQw2cxN'
, 'QmZ2hLRiB9DyCRadMnAvw7kueC1AYV8cCZyiSQNo7cffsc']

    
api_key = os.environ.get("PINATA_API_KEY")
secret_key = os.environ.get("PINATA_SECRET_API_KEY")
if api_key and secret_key:
    pinata = PinataPy(api_key, secret_key)
else:
    raise ValueError("No API keys in environment variables")
for cid in cids:
# response = pinata.pin_hash_to_ipfs(ipfs_hash_directory, f'{files[file]}')
    response = pinata.remove_pin_from_ipfs(cid)
    print(response)
