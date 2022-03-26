import os
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__))

#quad tl
tl_tl = 1 # top left
tl_tr = 2 # top right
tl_bl = 3 # bottom left
tl_br = 4 # bottom right

#quad tr
tr_tl = 7 # top left
tr_tr = 6 # top right
tr_bl = 5 # bottom left
tr_br = 8 # bottom right

#quad bl
bl_tl = 9 # top left
bl_tr = 10 # top right
bl_bl = 11 # bottom left
bl_br = 12 # bottom right

#quad br
br_tl = 13 # top left
br_tr = 14 # top right
br_bl = 16 # bottom left
br_br = 15 # bottom right


def main():
    for n in range(0, 72): #0,72

        frame = Image.new('RGB', (4720, 4720))# random solid

        tl_tl_img = Image.open(f"{dir_path}/output/raw/{tl_tl}/{tl_tl}_{n:03}.png")
        tl_tr_img = Image.open(f"{dir_path}/output/raw/{tl_tr}/{tl_tr}_{n:03}.png")
        tl_bl_img = Image.open(f"{dir_path}/output/raw/{tl_bl}/{tl_bl}_{n:03}.png")
        tl_br_img = Image.open(f"{dir_path}/output/raw/{tl_br}/{tl_br}_{n:03}.png")

        tr_tl_img = Image.open(f"{dir_path}/output/raw/{tr_tl}/{tr_tl}_{n:03}.png")
        tr_tr_img = Image.open(f"{dir_path}/output/raw/{tr_tr}/{tr_tr}_{n:03}.png")
        tr_bl_img = Image.open(f"{dir_path}/output/raw/{tr_bl}/{tr_bl}_{n:03}.png")
        tr_br_img = Image.open(f"{dir_path}/output/raw/{tr_br}/{tr_br}_{n:03}.png")

        bl_tl_img = Image.open(f"{dir_path}/output/raw/{bl_tl}/{bl_tl}_{n:03}.png")
        bl_tr_img = Image.open(f"{dir_path}/output/raw/{bl_tr}/{bl_tr}_{n:03}.png")
        bl_bl_img = Image.open(f"{dir_path}/output/raw/{bl_bl}/{bl_bl}_{n:03}.png")
        bl_br_img = Image.open(f"{dir_path}/output/raw/{bl_br}/{bl_br}_{n:03}.png")

        br_tl_img = Image.open(f"{dir_path}/output/raw/{br_tl}/{br_tl}_{n:03}.png")
        br_tr_img = Image.open(f"{dir_path}/output/raw/{br_tr}/{br_tr}_{n:03}.png")
        br_bl_img = Image.open(f"{dir_path}/output/raw/{br_bl}/{br_bl}_{n:03}.png")
        br_br_img = Image.open(f"{dir_path}/output/raw/{br_br}/{br_br}_{n:03}.png")

        #tl
        frame.paste(tl_tl_img, box=(0,0))
        frame.paste(tl_tr_img, box=(1180,0))
        frame.paste(tl_bl_img, box=(0,1180))
        frame.paste(tl_br_img, box=(1180,1180))

        #tr
        frame.paste(tr_tl_img, box=(2360,0))
        frame.paste(tr_tr_img, box=(3540,0))
        frame.paste(tr_bl_img, box=(2360,1180))
        frame.paste(tr_br_img, box=(3540,1180))

        #bl
        frame.paste(bl_tl_img, box=(0,2360))
        frame.paste(bl_tr_img, box=(1180,2360))
        frame.paste(bl_bl_img, box=(0,3540))
        frame.paste(bl_br_img, box=(1180,3540))

        #br
        frame.paste(br_tl_img, box=(2360,2360))
        frame.paste(br_tr_img, box=(3540,2360))
        frame.paste(br_bl_img, box=(2360,3540))
        frame.paste(br_br_img, box=(3540,3540))

        frame = frame.resize((2360, 2360))

        frame.save(f"{dir_path}/output/collage/collage_{n:03}.png", format="png") 
        
        print(f'Completed Frame #{n}!')

if __name__ == "__main__":
    main()
