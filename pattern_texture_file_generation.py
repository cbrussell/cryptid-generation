import os
import numpy as np
import sys
import fnmatch
from blend_modes import multiply
from PIL import Image
from pathlib import Path

color_opacity = {'black': ['#121A24', 0.4] ,'blue': ['#0257A5', 0.2], 'brown': ['#813513', 0.2], 'gray': ['#3E4C5E', 0.2], 'orange': ['#E24211', 0.2], 'purple': ['#3E2566', 0.4], 'red': ['#85000A', 0.2], 'white': ['#FDF7F2', 0.5], 'yellow': ['#Dc7F12', 0.2]}

##### user input for folder names to combine #####

# define name of folders for combining

base_folder = 'test_neckpattern_stripes_color'
texture_folder = 'test_neckpattern_stripes_texture'

base_file_name = 'neckpattern_stripes_color'
texture_file_name = 'neckpattern_stripes_texture'

combined_name = 'neckpattern_stripes_combined'

# define location of base and texture folder names 

base_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/RENDERS/{base_folder}/"
texture_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/RENDERS/{texture_folder}/"
combined_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/RENDERS/{combined_name}/"

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

for key in color_opacity:

    color_path = combined_path / f'{combined_name}_{key}'
    os.makedirs(color_path, exist_ok=True)

    for i in range(1, 73):

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
        blended_img_raw.save(color_path / f'neckpattern_stripes_{key}_{i:03}.png', format="png")
