import os
import numpy as np
import sys
import fnmatch
from datetime import datetime
from blend_modes import multiply
from PIL import Image
from pathlib import Path
from multiprocessing import Process, Manager

# future improvement
# write folder names and color opacities to list
# then increment over list with multiprocessing

def main():
   

    jobs = []
    with Manager() as manager:
        color_opacity = {'black': ['#121A24', 0.4] ,'blue': ['#0257A5', 0.2], 'brown': ['#813513', 0.2], 'gray': ['#3E4C5E', 0.2], 'orange': ['#E24211', 0.2], 'purple': ['#3E2566', 0.4], 'red': ['#85000A', 0.2], 'white': ['#FDF7F2', 0.10], 'yellow': ['#Dc7F12', 0.2]}
       
        # color_opacity = {'white': ['#FDF7F2', 0.10]}
        color_opacity = { 
        'brown':    [['#813513', 0.2], ['#813513', 0.25],['#813513', 0.40],['#813513', 0.7], ['#813513', 0.85]],
        'purple':   [['#3E2566', 0.4], ['#3E2566', 0.45], ['#3E2566', 0.6], ['#3E2566', 0.9], ['#3E2566', 1]],
        'black':    [['#121A24', 0.4], ['#121A24', 0.45], ['#121A24', 0.6], ['#121A24', 0.9], ['#121A24', 0.85]],
        'blue':     [['#0257A5', 0.2], ['#0257A5', 0.25], ['#0257A5', 0.40], ['#0257A5', 0.7], ['#0257A5', 0.85]],
        'red':      [['#85000A', 0.2], ['#85000A', 0.25], ['#85000A', 0.40], ['#85000A', 0.7], ['#85000A', 0.85]],
        'orange':   [['#E24211', 0.2], ['#E24211', 0.25], ['#E24211', 0.40], ['#E24211', 0.7], ['#E24211', 0.85]],
        'gray':     [['#3E4C5E', 0.2], ['#3E4C5E', 0.25], ['#3E4C5E', 0.40], ['#3E4C5E', 0.7], ['#3E4C5E', 0.85]],
        'yellow':   [['#DC7F12', 0.2], ['#DC7F12', 0.25], ['#DC7F12', 0.40], ['#DC7F12', 0.7], ['#DC7F12', 0.85]],
        'white':    [['#FDF7F2', 0.1], ['#FDF7F2', 0.15], ['#FDF7F2', 0.30], ['#FDF7F2', 0.6], ['#FDF7F2', 0.75]],
    }

        list = ['tailpattern_stripes_kitsune1', 'tailpattern_stripes_kitsune2','tailpattern_stripes_kitsune3','tailpattern_stripes_kitsune4','tailpattern_stripes_kitsune5',]
        
        # list = ['headpattern']

        ##### user input for folder names to combine #####
        # animals = ['lion_stripes', 'horse_stripes', 'wolf_stripes', 'bear_stripes', 'eagle_stripes']
        animals = ['lion'] # 'lion_stripes', 'horse_stripes', 'wolf_stripes', 'bear_stripes', 'eagle_stripes']
        # define name of folders for combining
        start_time = datetime.now()
        for kitsune_step, item in enumerate(list):
            for animal in animals:
                for color in color_opacity:
                # animal = 'eagle'
                    base_folder_name = f'{item}_color'                  # color folder
                    texture_folder_name = f'{item}_texture'  # texture folder
                    combined_name = f'{item}'  #f'torsopattern_stripes'

                    # define location of base and texture folder names 

                    base_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/{base_folder_name}/"
                    texture_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/{texture_folder_name}/"
                    combined_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/{combined_name}/"

                    # count number of pngs

                    base_list = fnmatch.filter(os.listdir(base_path), '*.png')
                    texture_list = fnmatch.filter(os.listdir(texture_path), '*.png')

                    #g et file count

                    base_frame_count = len(base_list)
                    texture_frame_count = len(texture_list)

                    # check for matching file counts
                    if base_frame_count != texture_frame_count:
                        sys.exit("Base frame and texture frame count do not match!")  


                    os.makedirs(combined_path, exist_ok=True)

                    
                    process = Process(target=worker, args=(color, combined_path, color_opacity, base_path, base_folder_name, texture_path, texture_folder_name, combined_name, kitsune_step))
                    jobs.append(process)
        [j.start() for j in jobs]
        [j.join() for j in jobs]

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f'Completed in {elapsed_time}.')

    return

def worker(key, combined_path, color_opacity, base_path, base_file_name, texture_path, texture_file_name, combined_name, kitsune_step):
    
       
    color_path = combined_path / f'{combined_name}_{key}'
    os.makedirs(color_path, exist_ok=True)
    for i in range(1, 73):
        print(f'Making frame {i} for {key}.')
        background_img_raw = Image.open(base_path / f'{base_file_name}_{i:03}.png')
        alpha = background_img_raw.getchannel('A')

        # give frame color
        background_img_raw = Image.new('RGBA', background_img_raw.size, color=color_opacity[key][kitsune_step][0])
        background_img_raw.putalpha(alpha)
        background_img = np.array(background_img_raw)  # Inputs to blend_modes need to be np arrays.
        background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
        # Import foreground image

        foreground_img_raw = Image.open(texture_path / f'{texture_file_name}_{i:03}.png')  # RGBA image
        foreground_img = np.array(foreground_img_raw)  # Inputs to blend_modes need to be np arrays.
        foreground_img_float = foreground_img.astype(float)  # Inputs to blend_modes need to be floats.
        # Blend images
        # opacity = 0.7  # The opacity of the foreground that is blended onto the background is 70 %.
        blended_img_float = multiply(background_img_float, foreground_img_float, color_opacity[key][kitsune_step][1])
        # Convert blended image back into PIL image
        blended_img = np.uint8(blended_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
        blended_img_raw = Image.fromarray(blended_img)
        # blended_img_raw.show()
        blended_img_raw.save(color_path / f'{combined_name}_{key}_{i:03}.png', format="png")

    print(f'Multiprocess job complete! Process ID is {os.getpid()}.')

if __name__ == "__main__":
    main()