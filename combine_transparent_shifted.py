import os
import numpy as np
from datetime import datetime
from numpy.core.multiarray import array
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from background import get_gradient, get_gradient_3d
from dna import Frames
from time import sleep
from background_2d_generator import get_2d_gradient
from collections import deque
from pathlib import Path 
import fnmatch
import shutil
import random

def combine_attributes(frames: Frames, prefix: str):
    # R = np.random.randint(0, 256)
    # G = np.random.randint(0, 256)
    # B = np.random.randint(0, 256)

    # R1 = np.random.randint(0, 256)
    # G1 = np.random.randint(0, 256)
    # B1 = np.random.randint(0, 256)
    
    # array = get_gradient_3d(1100, 1100, (R1, G1, B1), (R, G, B), (True, False, False)) # 4 way gradient

    # array = get_gradient()

    # use for 2d gradient
    # array = get_2d_gradient(R, G, B, R1, G1, B1)
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # use this for metadatabackground
    # for (n, background) in enumerate(frames.background_frames):
    # print("Generating frames...")

    for n in range(0, 72): #0,72

        # use this is background color
        # frame = Image.open(background) # background of data

        # 2d array
        # frame = Image.fromarray(np.uint8(array)).rotate(270)
    
        # 4 way gradient
        # frame = Image.fromarray(np.uint8(array))

        # frame = Image.new('RGB', (1180, 1180), (R, G, B)) # random solid
        

        # frame = Image.open(frames.background_frame[0]) # use chosen background from DNA

        # frame = Image.new('RGB', (1180, 1180), (0, 177, 64)) # green bg for transparency

        frame = Image.new('RGBA', (1100, 1100)) # make transparent background
        
       
        print(f'Generating frame {n}...')
        if frames.tail_frames:
            tail = Image.open(frames.tail_frames[n])
            frame = Image.alpha_composite(frame, tail)

        if frames.tailpattern_frames:
            tailpattern = Image.open(frames.tailpattern_frames[n])
            frame = Image.alpha_composite(frame, tailpattern)

        if frames.leftbackleg_frames:
            leftbackleg = Image.open(frames.leftbackleg_frames[n])
            frame = Image.alpha_composite(frame, leftbackleg)

        if frames.leftbacklegshadow_frames:
            leftbacklegshadow = Image.open(frames.leftbacklegshadow_frames[n])
            frame = Image.alpha_composite(frame, leftbacklegshadow )

        if frames.leftfrontleg_frames[n]:
            leftfrontleg = Image.open(frames.leftfrontleg_frames[n])
            frame = Image.alpha_composite(frame, leftfrontleg)

        if frames.leftfrontlegshadow_frames[n]:
            leftfrontlegshadow = Image.open(frames.leftfrontlegshadow_frames[n])
            frame = Image.alpha_composite(frame, leftfrontlegshadow )

        if frames.back_frames:
            back = Image.open(frames.back_frames[n])
            frame = Image.alpha_composite(frame, back)
       
        if frames.torsobase_frames:
            torsobase = Image.open(frames.torsobase_frames[n])
            frame = Image. alpha_composite(frame, torsobase)

        if frames.torsoaccent_frames:
            torsoaccent = Image.open(frames.torsoaccent_frames[n])
            frame = Image.alpha_composite(frame, torsoaccent )

        if frames.torsopattern_frames:
            torsopattern = Image.open(frames.torsopattern_frames[n])
            frame = Image.alpha_composite(frame, torsopattern)

        if frames.neckbase_frames:
            neckbase = Image.open(frames.neckbase_frames[n])
            frame = Image.alpha_composite(frame, neckbase)
        
        if frames.neckaccent_frames:
            neckaccent = Image.open(frames.neckaccent_frames[n])
            frame = Image.alpha_composite(frame, neckaccent)

        if frames.neckpattern_frames:
            neckpattern = Image.open(frames.neckpattern_frames[n])
            frame = Image.alpha_composite(frame, neckpattern)
        
        if frames.neckshadow_frames:
            neckshadow = Image.open(frames.neckshadow_frames[n])
            frame = Image.alpha_composite(frame, neckshadow)
        
        if frames.neckshadow_teeth_frames:
            neckshadow_teeth = Image.open(frames.neckshadow_teeth_frames[n])
            frame = Image.alpha_composite(frame, neckshadow_teeth)

        if frames.fur_frames:
            fur = Image.open(frames.fur_frames[n])
            frame = Image.alpha_composite(frame, fur)

        if frames.furshadow_frames:
            furshadow = Image.open(frames.furshadow_frames[n])
            frame = Image.alpha_composite(frame, furshadow)

        if frames.fur_shadow_teeth_frames:
            fur_shadow_teeth = Image.open(frames.fur_shadow_teeth_frames[n])
            frame = Image. alpha_composite(frame, fur_shadow_teeth)

        if frames.ear_shadow_fur_frames:
            ear_shadow_fur = Image.open(frames.ear_shadow_fur_frames[n])
            frame = Image.alpha_composite(frame, ear_shadow_fur)

        if frames.rightbackleg_frames:
            rightbackleg = Image.open(frames.rightbackleg_frames[n])
            frame = Image.alpha_composite(frame, rightbackleg)

        if frames.rightbackleg_pattern_frames:
            rightbackleg_pattern = Image.open(frames.rightbackleg_pattern_frames[n])
            frame = Image.alpha_composite(frame, rightbackleg_pattern)
        
        if frames.rightfrontleg_frames:
            rightfrontleg = Image.open(frames.rightfrontleg_frames[n])
            frame = Image.alpha_composite(frame, rightfrontleg)

        if frames.rightfrontleg_pattern_frames:
            rightfrontleg_pattern = Image.open(frames.rightfrontleg_pattern_frames[n])
            frame = Image.alpha_composite(frame, rightfrontleg_pattern)
        
        if frames.ears_frames:
            ears = Image.open(frames.ears_frames[n])
            frame = Image.alpha_composite(frame, ears)

        if frames.headbase_frames:
            headbase = Image.open(frames.headbase_frames[n])
            frame = Image.alpha_composite(frame, headbase)
        
        if frames.headaccent_frames:
            headaccent =Image.open(frames.headaccent_frames[n])
            frame = Image.alpha_composite(frame, headaccent)

        if frames.headpattern_frames:
            headpattern = Image.open(frames.headpattern_frames[n])
            frame = Image.alpha_composite(frame, headpattern)

        if frames.mouth_frames:
            mouth = Image.open(frames.mouth_frames[n])
            frame = Image.alpha_composite(frame, mouth)

        if frames.horns_frames:
            horns = Image.open(frames.horns_frames[n])
            frame = Image.alpha_composite(frame, horns)
        
        if frames.eyes_frames:
            eyes = Image.open(frames.eyes_frames[n])
            frame = Image.alpha_composite(frame, eyes)

        if n == 0:
            # time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transparent_resize = Image.new('RGBA', (1180, 1180))

            transparent_resize.paste(frame, box=(20, 70), mask=frame)

            width, height = transparent_resize.size
 
            # Setting the points for cropped image
            # center
            x, y = (881, 305)

            # pfp size
            width, height = (515, 515)
            left = x - width/2
            top = y - height/2
            right = x + width/2
            bottom = y + height/2 

            

            # draw = ImageDraw.Draw(transparent_resize)
            # leftUpPoint = (left, top)
            # rightDownPoint = (right, bottom)

            # twoPointList = [leftUpPoint, rightDownPoint]

            # draw.ellipse(twoPointList, fill=None, outline='yellow', width=5)

            # draw.line([(x, top + 5), (x, bottom - 5)], fill='black', width=5)

            # draw.line([(left + 5, y), (right - 5, y)], fill='black', width=5)



            transparent_resize.save(f"{dir_path}/output/stills/{prefix}_transparent.png")

            transparent_resize_crop = transparent_resize.crop((left, top, right, bottom))

            transparent_resize_crop.save(f"{dir_path}/output/stills/{prefix}_transparent_pfp.png")





        # background = Image.open(frames.background_frame[0]) # use chosen background from DNA

        background = Image.new('RGBA', (1180, 1180))
        # background = background.crop((40, 40, 1140, 1140))
        # background.paste(frame, box=(20, 70), mask=frame)
        
                

        # alpha = frame.getchannel('A')
        # frame = Image.new('RGBA', frame.size, color='black')
        # frame.putalpha(alpha) 
        background.paste(frame, box=(20, 70), mask=frame)



        # print("Almost there...")

        # watermark settings
        # find texts with "find {/System,}/Library/Fonts -name *ttf"
        ######

        # Width, Height = frame.size 
        # drawn = ImageDraw.Draw(frame) 
        # text = "test mint"
        # font = ImageFont.truetype("Arial Black", 138)
        # textwidth, textheight = drawn.textsize(text, font)
        # margin = 5
        # x = Width - textwidth
        # y = Height - textheight
        # drawn.text(((x/2), (y/2)), text, font=font) 

      
      

        frame = frame.convert("RGB")  

        background.save(f"{dir_path}/output/raw/{prefix}/{prefix}_{n:03}.png", format="png") 

        if n == 0:
            # time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    

            # draw = ImageDraw.Draw(background)
           
            # draw.ellipse(twoPointList, fill=None, outline='yellow', width=5)

            # draw.line([(x, top + 5), (x, bottom -5)], fill='black', width=5)

            # draw.line([(left +5, y), (right -5, y)], fill='black', width=5)

            background.save(f"{dir_path}/output/stills/{prefix}_solid.png")

            background_crop = background.crop((left, top, right, bottom))

            background_crop.save(f"{dir_path}/output/stills/{prefix}_solid_pfp.png")


            # frame = Image.fromarray(np.uint8(array)).rotate(270).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R1}_{G1}_{B1}_{R}_{G}_{B}.png", "PNG")
           
            # frame = Image.new('RGB', (1180, 1180), (R, G, B)).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R}_{G}_{B}.png", "PNG")
           
            # frame = Image.fromarray(np.uint8(array)).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R1}_{G1}_{B1}_{R}_{G}_{B}.png", "PNG")

  
    os.makedirs(f"{dir_path}/output/raw_shifted/{prefix}", exist_ok=True)
    # Determine image path
    json_path = Path(__file__).resolve().parents[1] / f"{dir_path}/output/raw/{prefix}"
    new_path = Path(__file__).resolve().parents[1] / f"{dir_path}/output/raw_shifted/{prefix}"

    # Renames image directory based on community generated shift-value
    shift_amount = random.randint(0, 72)
    print(f"Random shift amount for cryptid {prefix} is {shift_amount}.")
    
    json_list = fnmatch.filter(os.listdir(json_path), '*.png')
    sorted_json_list = sorted(json_list, key=lambda x: int(os.path.splitext(x)[0]))
    json_count = len(sorted_json_list)

    # Rotate list using deque
    deque_sorted_json_list = deque(sorted_json_list)
    deque_sorted_json_list.rotate(shift_amount)
    rotated_deque = list(deque_sorted_json_list)

    print(f"\nOriginal list is: {sorted_json_list}\n")
    print(f"\nShifted list is: {rotated_deque}\n")
    print(f"\nShift amount is: {shift_amount}\n")



    # Replace original files for new name (changing folders)
    for i in range(json_count):
        new_name = Path(new_path / rotated_deque[i]) #file
        original_name = Path(json_path / sorted_json_list[i]) #location
        shutil.copy(original_name, new_name)
