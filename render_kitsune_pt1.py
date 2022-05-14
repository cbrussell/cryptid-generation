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

        base_list = ['tail_kitsune1', 'tail_kitsune2', 'tail_kitsune3', 'tail_kitsune4', 'tail_kitsune5']
        
      
        # define name of folders for combining
        start_time = datetime.now()
        for item in base_list:
            for color in color_opacity:
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
                
                process = Process(target=worker, args=(color, combined_path, color_opacity, base_path, base_folder_name, texture_path, texture_folder_name, combined_name))
                jobs.append(process)
        [j.start() for j in jobs]
        [j.join() for j in jobs]

        stripe_list = ['tailpattern_stripes_kitsune1','tailpattern_stripes_kitsune2', 'tailpattern_stripes_kitsune3', 'tailpattern_stripes_kitsune4', 'tailpattern_stripes_kitsune5' ]

        # combine kitsunes into one frame, no color adding, just layt
        
        for color in color_opacity:
            base_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/{item}_{color}/"
            combined_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune_{color}/"
            # count number of pngs
            base_list = fnmatch.filter(os.listdir(base_path), '*.png')
           
            base_frame_count = len(base_list)
            if base_frame_count != 72:
                sys.exit("Not enough eye frames in file")  
            os.makedirs(combined_path, exist_ok=True)
            
            process = Process(target=worker_combine, args=(color, combined_path, base_path))
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

def worker_combine(color, combined_path, base_path):
    
    # new folder for each color
    # color_path = combined_path / f'tail_kitsune_{color}'

    os.makedirs(combined_path, exist_ok=True)
    for i in range(1, 73):
        print(f'Making frame {i} for {color}.')
        # eyes = Image.open(base_path / f'{item}_{i:03}.png')
        # alpha = eyes.getchannel('A')

        # give frame color
        # eyes = Image.new('RGBA', eyes.size, color=eye_colors[color])
        # eyes.putalpha(alpha)
        # eyes.save(color_path / f'{item}_{color}_{i:03}.png', format="png")

        # frame = Image.new('RGBA', (1100, 1100)) # make transparent background

        tail_layer_5 = Image.open(base_path / f'tail_kitsune5_{color}_{i:03}.png')
        tail_layer_4 = Image.open(base_path / f'tail_kitsune4_{color}_{i:03}.png')
        tail_layer_3 = Image.open(base_path / f'tail_kitsune3_{color}_{i:03}.png')
        tail_layer_2 = Image.open(base_path / f'tail_kitsune2_{color}_{i:03}.png')
        tail_layer_1 = Image.open(base_path / f'tail_kitsune1_{color}_{i:03}.png')

        com1 = Image.alpha_composite(tail_layer_5, tail_layer_4)
        com2 = Image.alpha_composite(com1, tail_layer_3)
        com3 = Image.alpha_composite(com2, tail_layer_2)
        com4 = Image.alpha_composite(com3, tail_layer_1)

        com4.save(combined_path / f'tail_kitsune_{color}_{i:03}.png', format="png")


    print(f'Multiprocess job complete! Process ID is {os.getpid()}.')

if __name__ == "__main__":
    main()