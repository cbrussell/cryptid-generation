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
        color_opacity = {'white': ['#FDF7F2', 0.10]}

        list = ['neckpattern_stripes', 'torsopattern_stripes', 'tailpattern_stripes_snake', 'tailpattern_stripes_lion', 'tailpattern_stripes_horse', 'tailpattern_stripes_scorpion']
        ##### user input for folder names to combine #####
        animals = ['lion']
        # define name of folders for combining
        start_time = datetime.now()
        for color in color_opacity:
            for layer in list:
                # animal = 'eagle'
                base_folder_name = f'{layer}_color'                  # color folder
                texture_folder_name = f'{layer}_texture'  # texture folder
                combined_name = layer  #f'torsopattern_stripes'
    
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
            
    
    
                        
                process = Process(target=worker, args=(color, combined_path, color_opacity, base_path, base_folder_name, texture_path, texture_folder_name, combined_name))
                jobs.append(process)
        [j.start() for j in jobs]
        [j.join() for j in jobs]

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f'Completed in {elapsed_time}.')

    return

def worker(key, combined_path, color_opacity, base_path, base_file_name, texture_path, texture_file_name, combined_name):
    
       
    color_path = combined_path / f'{combined_name}_{key}'
    os.makedirs(color_path, exist_ok=True)
    for i in range(1, 73):
        print(f'Making frame {i} for {key}.')
        background_img_raw = Image.open(base_path / f'{base_file_name}_{i:03}.png')
        alpha = background_img_raw.getchannel('A')

        # give frame color
        background_img_raw = Image.new('RGBA', background_img_raw.size, color=color_opacity[key][0])
        background_img_raw.putalpha(alpha)
        background_img = np.array(background_img_raw)  # Inputs to blend_modes need to be np arrays.
        background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
        # Import foreground image

        foreground_img_raw = Image.open(texture_path / f'{texture_file_name}_{i:03}.png')  # RGBA image
        foreground_img = np.array(foreground_img_raw)  # Inputs to blend_modes need to be np arrays.
        foreground_img_float = foreground_img.astype(float)  # Inputs to blend_modes need to be floats.
        # Blend images
        # opacity = 0.7  # The opacity of the foreground that is blended onto the background is 70 %.
        blended_img_float = multiply(background_img_float, foreground_img_float, color_opacity[key][1])
        # Convert blended image back into PIL image
        blended_img = np.uint8(blended_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
        blended_img_raw = Image.fromarray(blended_img)
        # blended_img_raw.show()
        blended_img_raw.save(color_path / f'{combined_name}_{key}_{i:03}.png', format="png")

    print(f'Multiprocess job complete! Process ID is {os.getpid()}.')

if __name__ == "__main__":
    main()