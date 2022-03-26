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