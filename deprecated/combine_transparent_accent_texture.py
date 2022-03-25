import os
import numpy as np
from datetime import datetime
from blend_modes import multiply
import random
from numpy.core.multiarray import array
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from deprecated.background import get_gradient, get_gradient_3d
from dna import Frames
from time import sleep
from background_2d_generator import get_2d_gradient

def combine_attributes(frames: Frames, prefix: str):
    R = np.random.randint(0, 256)
    G = np.random.randint(0, 256)
    B = np.random.randint(0, 256)

    opacity = round(random.random(), 2)
    print(opacity)
    pattern_color = (R, G, B)

    outFile = open('colors.txt', 'a')
    outFile.write(f'{pattern_color} - {opacity}\n')
    outFile.close()


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

    for n in range(0, 1): #0,72

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

            # frame = Image. alpha_composite(frame,tail tail)

        if frames.tailpattern_frames:
            # print(frames.tailpattern_frames[n])
            tailpattern = Image.open(frames.tailpattern_frames[n])
            frame = Image.alpha_composite(frame, tailpattern)

            # frame = Image. alpha_composite(frame,tailpattern tailpattern)

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
            
        if frames.torsoaccent_frames:
            torsoaccent = Image.open(frames.torsoaccent_frames[n])
         

            # alpha = torsoaccent.getchannel('A')
            # torsoaccent = Image.new('RGBA', torsoaccent.size, color=accent_color)
            # torsoaccent.putalpha(alpha) 


           

            frame = Image.alpha_composite(frame, torsoaccent )

        if frames.torsopattern_frames:
            torsopattern = Image.open(frames.torsopattern_frames[n])
            frame = Image.alpha_composite(frame, torsopattern)

        if frames.neckbase_frames:
            neckbase = Image.open(frames.neckbase_frames[n])
            frame = Image.alpha_composite(frame, neckbase)
        
        if frames.neckaccent_frames:
            neckaccent = Image.open(frames.neckaccent_frames[n])

            # alpha = neckaccent.getchannel('A')
            # neckaccent = Image.new('RGBA', neckaccent.size, color=accent_color)
            # neckaccent.putalpha(alpha)
            # frame = Image.alpha_composite(frame, neckaccent)

        # if frames.neckpattern_frames:
            # neckpattern = Image.open(frames.neckpattern_frames[n])

            # Import background image

            # get frame

        background_img_raw = Image.open(f'{dir_path}/RENDERS/test_neckpattern_stripes_color/neckpattern_stripes_color_001.png') 
            
           

        alpha = background_img_raw.getchannel('A')

        # give frame color
        background_img_raw = Image.new('RGBA', background_img_raw.size, color=pattern_color)

        background_img_raw.putalpha(alpha)
        background_img = np.array(background_img_raw)  # Inputs to blend_modes need to be np arrays.
        background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
        # Import foreground image
        foreground_img_raw = Image.open(f'{dir_path}/RENDERS/test_neckpattern_stripes_texture/neckpattern_stripes_texture_001.png')  # RGBA image
        foreground_img = np.array(foreground_img_raw)  # Inputs to blend_modes need to be np arrays.
        foreground_img_float = foreground_img.astype(float)  # Inputs to blend_modes need to be floats.
        # Blend images
        # opacity = 0.7  # The opacity of the foreground that is blended onto the background is 70 %.
        blended_img_float = multiply(background_img_float, foreground_img_float, opacity)
        # Convert blended image back into PIL image
        blended_img = np.uint8(blended_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
        neckpattern = Image.fromarray(blended_img)
        # neckpattern.show()

        # break

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
           
            # alpha = headaccent.getchannel('A')
            # headaccent = Image.new('RGBA', headaccent.size, color=accent_color)
            # headaccent.putalpha(alpha)

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
            frame.save(f"{dir_path}/output/stills/{prefix}_transparent.png")


        background = Image.open(frames.background_frame[0]) # use chosen background from DNA
        # background = background.crop((40, 40, 1140, 1140))
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
            background.save(f"{dir_path}/output/stills/{prefix}_solid.png")


            # frame = Image.fromarray(np.uint8(array)).rotate(270).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R1}_{G1}_{B1}_{R}_{G}_{B}.png", "PNG")
           
            # frame = Image.new('RGB', (1180, 1180), (R, G, B)).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R}_{G}_{B}.png", "PNG")
           
            # frame = Image.fromarray(np.uint8(array)).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R1}_{G1}_{B1}_{R}_{G}_{B}.png", "PNG")

    