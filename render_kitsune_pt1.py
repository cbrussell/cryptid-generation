import os
import numpy as np
import sys
import fnmatch
from datetime import datetime
from blend_modes import multiply, soft_light
from PIL import Image
from pathlib import Path
from multiprocessing import Process, Manager

def main():
    color_opacity = { 
        'brown':    [['#c35824', 0.2], ['#a9431e', 0.25],['#a9431e', 0.40],['#a9431e', 0.7], ['#813513', 0.85]],
        'purple':   [['#7037D9', 0.2], ['#572CA2', 0.25], ['#572CA2', 0.40], ['#572CA2', 0.7], ['#3E2566', 0.85]],
        'black':    [['#2A3A3F', 0.2], ['#1E2D37', 0.25], ['#1E2D37', 0.40], ['#1E2D37', 0.7], ['#121A24', 0.85]],
        'blue':     [['#0196C7', 0.2], ['#0178B7', 0.25], ['#0178B7', 0.40], ['#0178B7', 0.7], ['#0257A5', 0.85]],
        'red':      [['#DC0017', 0.2], ['#B00010', 0.25], ['#B00010', 0.40], ['#B00010', 0.7], ['#85000A', 0.85]],
        'orange':   [['#F47813', 0.2], ['#EA5F14', 0.25], ['#EA5F14', 0.40], ['#EA5F14', 0.7], ['#E24211', 0.85]],
        'gray':     [['#7C92A2', 0.2], ['#5C7081', 0.25], ['#5C7081', 0.40], ['#5C7081', 0.7], ['#3E4C5E', 0.85]],
        'yellow':   [['#F5B722', 0.2], ['#E69B18', 0.25], ['#E69B18', 0.40], ['#E69B18', 0.7], ['#DC7F12', 0.85]],
        'white':    [['#FFF1E6', 0.2], ['#E9D8CF', 0.25], ['#E9D8CF', 0.40], ['#E9D8CF', 0.7], ['#B8A49A', 0.85]],
    }


    jobs = []
    with Manager() as manager:
       
        base_list = ['tail_kitsune1', 'tail_kitsune2', 'tail_kitsune3', 'tail_kitsune4', 'tail_kitsune5' ]
        
        start_time = datetime.now()
        for i, item in enumerate(base_list):
            for color in color_opacity:
                base_folder_name = f'{item}_color'                  # color folder
                texture_folder_name = f'{item}_texture'  # texture folder
                combined_name = f'{item}'  #f'torsopattern_stripes'
          

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
                
                process = Process(target=worker, args=(color, combined_path, color_opacity, base_path, base_folder_name, texture_path, texture_folder_name, combined_name, i))
                jobs.append(process)
        [j.start() for j in jobs]
        [j.join() for j in jobs]

        # combine kitsunes into one frame, no color adding, just layt
        

    jobs = []
    with Manager() as manager:
        # color_opacity = {'black': ['#121A24', 0.4] ,'blue': ['#0257A5', 0.2], 'brown': ['#813513', 0.2], 'gray': ['#3E4C5E', 0.2], 'orange': ['#E24211', 0.2], 'purple': ['#3E2566', 0.4], 'red': ['#85000A', 0.2], 'white': ['#FDF7F2', 0.10], 'yellow': ['#Dc7F12', 0.2]}
        # color_opacity = {'brown': ['#813513', 0.2]}
        start_time = datetime.now()
        for color in color_opacity:
            combined_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune_{color}/"
            os.makedirs(combined_path, exist_ok=True)
            process = Process(target=worker_combine, args=(color, combined_path))
            jobs.append(process)
        [j.start() for j in jobs]
        [j.join() for j in jobs]

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f'Completed in {elapsed_time}.')

    return

def worker(key, combined_path, color_opacity, base_path, base_file_name, texture_path, texture_file_name, combined_name, tail_number):
    
       
    color_path = combined_path / f'{combined_name}_{key}'
    os.makedirs(color_path, exist_ok=True)
    for i in range(1, 73):
        print(f'Making frame {i} for {key}.')
        background_img_raw = Image.open(base_path / f'{base_file_name}_{i:03}.png').convert('RGBA')
        alpha = background_img_raw.getchannel('A')

        # give frame color
        print(i)
        background_img_raw = Image.new('RGBA', background_img_raw.size, color=color_opacity[key][tail_number][0])
        background_img_raw.putalpha(alpha)
        background_img = np.array(background_img_raw)  # Inputs to blend_modes need to be np arrays.
        background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
        # Import foreground image

        foreground_img_raw = Image.open(texture_path / f'{texture_file_name}_{i:03}.png').convert('RGBA')  # RGBA image
        # foreground_img_raw.putalpha(255) 
        foreground_img = np.array(foreground_img_raw)
        
         # Inputs to blend_modes need to be np arrays.
        foreground_img_float = foreground_img.astype(float)  # Inputs to blend_modes need to be floats.
        # Blend images
        # opacity = 0.7  # The opacity of the foreground that is blended onto the background is 70 %.
        
        # opacity = color_opacity[key][1] + (( 1 - color_opacity[key][1]) / 4 ) * opacity_steps 
        # print(f'Color is {key} and opacity is {opacity}. Opacity step {opacity_steps}.')
        print(f'{color_opacity[key][tail_number][1]} is the opacity for {base_path}')
        blended_img_float = multiply(background_img_float, foreground_img_float, color_opacity[key][tail_number][1])
        # Convert blended image back into PIL image
        blended_img = np.uint8(blended_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
        blended_img_raw = Image.fromarray(blended_img)
        # blended_img_raw.show()
        blended_img_raw.save(color_path / f'{combined_name}_{key}_{i:03}.png', format="png")

    print(f'Multiprocess job complete! Process ID is {os.getpid()}.')

def worker_combine(color, combined_path):

    os.makedirs(combined_path, exist_ok=True)
    for i in range(1, 73):
        print(f'Making frame {i} for {color}.')

        base_path_5 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune5/tail_kitsune5_{color}/"
        base_path_4 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune4/tail_kitsune4_{color}/"
        base_path_3 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune3/tail_kitsune3_{color}/"
        base_path_2 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune2/tail_kitsune2_{color}/"
        base_path_1 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune1/tail_kitsune1_{color}/"

        tail_layer_5 = Image.open(base_path_5 / f'tail_kitsune5_{color}_{i:03}.png').convert('RGBA')
        tail_layer_4 = Image.open(base_path_4 / f'tail_kitsune4_{color}_{i:03}.png').convert('RGBA')
        tail_layer_3 = Image.open(base_path_3 / f'tail_kitsune3_{color}_{i:03}.png').convert('RGBA')
        tail_layer_2 = Image.open(base_path_2 / f'tail_kitsune2_{color}_{i:03}.png').convert('RGBA')
        tail_layer_1 = Image.open(base_path_1 / f'tail_kitsune1_{color}_{i:03}.png').convert('RGBA')

        com1 = Image.alpha_composite(tail_layer_5, tail_layer_4)
        com2 = Image.alpha_composite(com1, tail_layer_3)
        com3 = Image.alpha_composite(com2, tail_layer_2)
        com4 = Image.alpha_composite(com3, tail_layer_1)

        com4.save(combined_path / f'tail_kitsune_{color}_{i:03}.png', format="png")

    print(f'Multiprocess job complete! Process ID is {os.getpid()}.')

if __name__ == "__main__":
    main()