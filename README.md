## Methodology
1. `trait_manifest.json`, `color_manifest.json`, and  `background_manifest.json` determine the rarity and occurance of traits tht form a single Cryptid.
2. Our files are 72 rendered frames (3 second animation), using the same naming convention for the folder and file. For example `eyes_beast_pupil_right` folder contains 72 files of `eyes_beast_pupil_right_00X.png`.
3. `generate.py` kicks off the automation with multiprocessing, recording the hashed dictionary of attributes to keep prevent duplicat.e Cryptids.
4. `dna.py` returns the metadata and list of trait file paths for the cryptids, to be used by `render_assets.py` for art generation (mp4, png, gif). At the end of this process, the dna is compared to `incompatible.py` to prevent clashing colors/attributes ex.) dark cryptid on a dark background.
5. `traits.py` contain all of the getter functions - which each chose the next layer of the cryptid based on complete chance, or input from another trait. 
6. `combine.py` layers all of the frames together, savings frames for transparent still images and pfp headshots. Both transparent and solid background animations were generated. 
7. `render_assets.py` combines the frames into multiple file formats using ffmpeg.


## Repo Installation Instructions
1. Clone repo into folder
2. pip install -r requirements.txt  

## Generate Cryptids 
1. Select number of frames and processes in `generate.py`
2. Run `generate.py`
3. Create assets with `render_assets.py`   


## Pin folder to IPFS Example  
```
ipfs add --recursive --progress ./gif  
```    