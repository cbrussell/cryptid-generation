import os
import numpy as np
from datetime import datetime
from numpy.core.multiarray import array
from PIL import Image, ImageFont, ImageDraw
from background import get_gradient, get_gradient_3d
from dna import Frames
from time import sleep
from background_2d_generator import get_2d_gradient

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

    for n in range(0, 1): #0,72

        # use this is background color
        # frame = Image.open(background) # background of data

        # 2d array
        # frame = Image.fromarray(np.uint8(array)).rotate(270)
    
        # 4 way gradient
        # frame = Image.fromarray(np.uint8(array))

        # frame = Image.new('RGB', (1180, 1180), (R, G, B)) # random solid
        

        frame = Image.open(frames.background_frame[0]) # use chosen background from DNA

        # frame = Image.new('RGB', (1180, 1180), (255, 245, 225)) # black bg

        if frames.tail_frames:
            print(frames.tail_frames[n])
            tail = Image.open(frames.tail_frames[n])
            frame.paste(tail, box=(20, 70), mask=tail)

        if frames.leftbackleg_frames:
            leftbackleg = Image.open(frames.leftbackleg_frames[n])
            frame.paste(leftbackleg, box=(20, 70), mask=leftbackleg)

        if frames.leftbacklegshadow_frames:
            leftbacklegshadow = Image.open(frames.leftbacklegshadow_frames[n])
            frame.paste(leftbacklegshadow, box=(20, 70), mask=leftbacklegshadow)

        if frames.leftfrontleg_frames[n]:
            leftfrontleg = Image.open(frames.leftfrontleg_frames[n])
            frame.paste(leftfrontleg, box=(20, 70), mask=leftfrontleg)

        if frames.leftfrontlegshadow_frames[n]:
            leftfrontlegshadow = Image.open(frames.leftfrontlegshadow_frames[n])
            frame.paste(leftfrontlegshadow, box=(20, 70), mask=leftfrontlegshadow)

        if frames.back_frames:
            back = Image.open(frames.back_frames[n])
            frame.paste(back, box=(20, 70), mask=back)
       
        if frames.torsobase_frames:
            torsobase = Image.open(frames.torsobase_frames[n])
            frame.paste(torsobase, box=(20, 70), mask=torsobase)

        if frames.torsoaccent_frames:
            torsoaccent = Image.open(frames.torsoaccent_frames[n])
            torsoaccent = torsoaccent
            frame.paste(torsoaccent, box=(20, 70), mask=torsoaccent)

        if frames.torsopattern_frames:
            torsopattern = Image.open(frames.torsopattern_frames[n])
            frame.paste(torsopattern, box=(20, 70), mask=torsopattern)

        if frames.neckbase_frames:
            neckbase = Image.open(frames.neckbase_frames[n])
            frame.paste(neckbase, box=(20, 70), mask=neckbase)
        
        if frames.neckaccent_frames:
            neckaccent = Image.open(frames.neckaccent_frames[n])
            frame.paste(neckaccent, box=(20, 70), mask=neckaccent)

        if frames.neckpattern_frames:
            neckpattern = Image.open(frames.neckpattern_frames[n])
            frame.paste(neckpattern, box=(20, 70), mask=neckpattern)
        
        if frames.neckshadow_frames:
            neckshadow = Image.open(frames.neckshadow_frames[n])
            frame.paste(neckshadow, box=(20, 70), mask=neckshadow)

        if frames.fur_frames:
            fur = Image.open(frames.fur_frames[n])
            frame.paste(fur, box=(20, 70), mask=fur)

        if frames.furshadow_frames:
            furshadow = Image.open(frames.furshadow_frames[n])
            frame.paste(furshadow, box=(20, 70), mask=furshadow)

        if frames.rightbackleg_frames:
            rightbackleg = Image.open(frames.rightbackleg_frames[n])
            frame.paste(rightbackleg, box=(20, 70), mask=rightbackleg)
        
        if frames.rightfrontleg_frames:
            rightfrontleg = Image.open(frames.rightfrontleg_frames[n])
            frame.paste(rightfrontleg, box=(20, 70), mask=rightfrontleg)

        if frames.ears_frames:
            ears = Image.open(frames.ears_frames[n])
            frame.paste(ears, box=(20, 70), mask=ears)

        if frames.headbase_frames:
            headbase = Image.open(frames.headbase_frames[n])
            frame.paste(headbase, box=(20, 70), mask=headbase)
        
        if frames.headaccent_frames:
            headaccent = Image.open(frames.headaccent_frames[n])
            frame.paste(headaccent, box=(20, 70), mask=headaccent)

        if frames.headpattern_frames:
            headpattern = Image.open(frames.headpattern_frames[n])
            frame.paste(headpattern, box=(20, 70), mask=headpattern)

        if frames.mouth_frames:
            mouth = Image.open(frames.mouth_frames[n])
            frame.paste(mouth, box=(20, 70), mask=mouth)

        if frames.horns_frames:
            horns = Image.open(frames.horns_frames[n])
            frame.paste(horns, box=(20, 70), mask=horns)
        
        if frames.eyes_frames:
            eyes = Image.open(frames.eyes_frames[n])
            frame.paste(eyes, box=(20, 70), mask=eyes)

        print("Almost there...")

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

        #####


        frame.save(f"{dir_path}/output/raw/{prefix}/{prefix}_{n:03}.png", format="png") 

        if n == 0:
            # time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            frame.save(f"{dir_path}/output/stills/{prefix}.png")


            # frame = Image.fromarray(np.uint8(array)).rotate(270).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R1}_{G1}_{B1}_{R}_{G}_{B}.png", "PNG")
           
            # frame = Image.new('RGB', (1180, 1180), (R, G, B)).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R}_{G}_{B}.png", "PNG")
           
            # frame = Image.fromarray(np.uint8(array)).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R1}_{G1}_{B1}_{R}_{G}_{B}.png", "PNG")

    