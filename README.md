Repo Installation Instructions
1. Clone repo into folder
2. pip install -r requirements.txt

Genrate Cryptids
1. Select number of frames in combined_transparent_shifted.py 
2. Select number of Cryptids in generate.py
3. Run generate.py

## Instructions for launch
1. Generate collection.
2. Calculate provenance hash based on image stills, freeze in contract.
3. Shift values based on community input.
4. Shift json and video filenames
5. Upload stills for Still CID
5. Upload MP4s for Video CID
6. Run metadata generation with stills and mp4 CIDs.
7. Upload pre-reveal jsons to IPFS (8888 files)
8. Based on reveal intention, replace pre-reveal jsons with final jsons
9. At reveal, upload mix of final and pre-reveal jsons to IPFS
10. Update baseURI
11. Once sold out, freeze baseURI.

## Dry run

1. Mint 777
2. Upload data for 1,111
3. Upload contract
4. Upload placeholder to IPFS
5. Merkle root for final collection
6. Airdrops
7. Mint whitelist
8. Mint secondary
9. Mint team supply
10. Mint public
11. Complete mint
12. Upload metadata
13. Figure out how to host own IPFS - need at least 5 tb

```shell
scp -i "/Users/chrisrussell/.ssh/ec2/cryptids_keypair_may_21.pem" -r mp4  ubuntu@ec2-3-21-33-226.us-east-2.compute.amazonaws.com:~
```
