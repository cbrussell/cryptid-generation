import os
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__))

tl = 7 # top left
tr = 11 # top right
bl = 140 # bottom left
br = 91 # bottom right

def main():
    for n in range(0, 1): #0,72
        os.makedirs(f"{dir_path}/output/collage", exist_ok=True)
        frame = Image.new('RGB', (2360, 2360))# random solid

        tl_img = Image.open(f"{dir_path}/output/raw/{tl}/{tl}_{n:03}.png")
        tr_img = Image.open(f"{dir_path}/output/raw/{tr}/{tr}_{n:03}.png")
        bl_img = Image.open(f"{dir_path}/output/raw/{bl}/{bl}_{n:03}.png")
        br_img = Image.open(f"{dir_path}/output/raw/{br}/{br}_{n:03}.png")

        # tl_img = Image.open(f"{dir_path}/output/stills/{tl}.png")
        # tr_img = Image.open(f"{dir_path}/output/stills/{tr}.png")
        # bl_img = Image.open(f"{dir_path}/output/stills/{bl}.png")
        # br_img = Image.open(f"{dir_path}/output/stills/{br}.png")


        frame.paste(tl_img, box=(0,0))
        frame.paste(tr_img, box=(1180,0))
        frame.paste(bl_img, box=(0,1180))
        frame.paste(br_img, box=(1180,1180))

        frame.save(f"{dir_path}/output/collage/collage_{n:03}.png", format="png") 
        
        print(f'Completed Frame #{n}!')

if __name__ == "__main__":
    main()
