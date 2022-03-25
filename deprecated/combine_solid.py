import os
import numpy as np
from datetime import datetime
from numpy.core.multiarray import array
from PIL import Image, ImageFont, ImageDraw
from deprecated.background import get_gradient, get_gradient_3d
from dna import Frames
from time import sleep
from background_2d_generator import get_2d_gradient

def combine_attributes_solid(frames: Frames, prefix: str):
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

        # frame = Image.new('RGB', (1180, 1180), (0, 177, 64)) # black bg

        solid_color = 'white'

        if frames.tail_frames:
            print(frames.tail_frames[n])
            tail = Image.open(frames.tail_frames[n])

            alpha = tail.getchannel('A')
            tail = Image.new('RGBA', tail.size, color=solid_color)
            tail.putalpha(alpha) 

            frame.paste(tail, box=(20, 70), mask=tail)

        if frames.leftbackleg_frames:
            leftbackleg = Image.open(frames.leftbackleg_frames[n])
            alpha = leftbackleg.getchannel('A')
            leftbackleg = Image.new('RGBA', leftbackleg.size, color=solid_color)
            leftbackleg.putalpha(alpha) 
            frame.paste(leftbackleg, box=(20, 70), mask=leftbackleg)

        if frames.leftbacklegshadow_frames:
            leftbacklegshadow = Image.open(frames.leftbacklegshadow_frames[n])
            frame.paste(leftbacklegshadow, box=(20, 70), mask=leftbacklegshadow)

        if frames.leftfrontleg_frames[n]:
            leftfrontleg = Image.open(frames.leftfrontleg_frames[n])
            alpha = leftfrontleg.getchannel('A')
            leftfrontleg = Image.new('RGBA', leftfrontleg.size, color=solid_color)
            leftfrontleg.putalpha(alpha) 
            frame.paste(leftfrontleg, box=(20, 70), mask=leftfrontleg)

        if frames.leftfrontlegshadow_frames[n]:
            leftfrontlegshadow = Image.open(frames.leftfrontlegshadow_frames[n])
            frame.paste(leftfrontlegshadow, box=(20, 70), mask=leftfrontlegshadow)

        if frames.back_frames:
            back = Image.open(frames.back_frames[n])
            alpha = back.getchannel('A')
            back = Image.new('RGBA', back.size, color=solid_color)
            back.putalpha(alpha) 
            frame.paste(back, box=(20, 70), mask=back)
       
        if frames.torsobase_frames:
            torsobase = Image.open(frames.torsobase_frames[n])
            alpha = torsobase.getchannel('A')
            torsobase = Image.new('RGBA', torsobase.size, color=solid_color)
            torsobase.putalpha(alpha) 
            frame.paste(torsobase, box=(20, 70), mask=torsobase)

        if frames.torsoaccent_frames:
            torsoaccent = Image.open(frames.torsoaccent_frames[n])
            alpha = torsoaccent.getchannel('A')
            torsoaccent = Image.new('RGBA', torsoaccent.size, color=solid_color)
            torsoaccent.putalpha(alpha) 
            frame.paste(torsoaccent, box=(20, 70), mask=torsoaccent)

        if frames.torsopattern_frames:
            torsopattern = Image.open(frames.torsopattern_frames[n])

            alpha = torsopattern.getchannel('A')
            torsopattern = Image.new('RGBA', torsopattern.size, color=solid_color)
            torsopattern.putalpha(alpha)

            frame.paste(torsopattern, box=(20, 70), mask=torsopattern)

        if frames.neckbase_frames:
            neckbase = Image.open(frames.neckbase_frames[n])
            alpha = neckbase.getchannel('A')
            neckbase = Image.new('RGBA', neckbase.size, color=solid_color)
            neckbase.putalpha(alpha)
            frame.paste(neckbase, box=(20, 70), mask=neckbase)
        
        if frames.neckaccent_frames:
            neckaccent = Image.open(frames.neckaccent_frames[n])
            alpha = neckaccent.getchannel('A')
            neckaccent = Image.new('RGBA', neckaccent.size, color=solid_color)
            neckaccent.putalpha(alpha)
            frame.paste(neckaccent, box=(20, 70), mask=neckaccent)

        if frames.neckpattern_frames:
            neckpattern = Image.open(frames.neckpattern_frames[n])
            alpha = neckpattern.getchannel('A')
            neckpattern = Image.new('RGBA', neckpattern.size, color=solid_color)
            neckpattern.putalpha(alpha)
            frame.paste(neckpattern, box=(20, 70), mask=neckpattern)
        
        if frames.neckshadow_frames:
            neckshadow = Image.open(frames.neckshadow_frames[n])

            # alpha = neckshadow.getchannel('A')
            # neckshadow = Image.new('RGBA', neckshadow.size, color=solid_color)
            # neckshadow.putalpha(alpha)

            frame.paste(neckshadow, box=(20, 70), mask=neckshadow)

        if frames.fur_frames:
            fur = Image.open(frames.fur_frames[n])
            
            alpha = fur.getchannel('A')
            fur = Image.new('RGBA', fur.size, color=solid_color)
            fur.putalpha(alpha)

            frame.paste(fur, box=(20, 70), mask=fur)

        if frames.furshadow_frames:
            furshadow = Image.open(frames.furshadow_frames[n])
            frame.paste(furshadow, box=(20, 70), mask=furshadow)

        if frames.rightbackleg_frames:
            rightbackleg = Image.open(frames.rightbackleg_frames[n])
            alpha = rightbackleg.getchannel('A')
            rightbackleg = Image.new('RGBA', rightbackleg.size, color=solid_color)
            rightbackleg.putalpha(alpha)
            frame.paste(rightbackleg, box=(20, 70), mask=rightbackleg)
        
        if frames.rightfrontleg_frames:
            rightfrontleg = Image.open(frames.rightfrontleg_frames[n])
            alpha = rightfrontleg.getchannel('A')
            rightfrontleg = Image.new('RGBA', rightfrontleg.size, color=solid_color)
            rightfrontleg.putalpha(alpha)
            frame.paste(rightfrontleg, box=(20, 70), mask=rightfrontleg)

        if frames.ears_frames:
            ears = Image.open(frames.ears_frames[n])
            alpha = ears.getchannel('A')
            ears = Image.new('RGBA', ears.size, color=solid_color)
            ears.putalpha(alpha)
            frame.paste(ears, box=(20, 70), mask=ears)

        if frames.headbase_frames:
            headbase = Image.open(frames.headbase_frames[n])
            alpha = headbase.getchannel('A')
            headbase = Image.new('RGBA', headbase.size, color=solid_color)
            headbase.putalpha(alpha)
            frame.paste(headbase, box=(20, 70), mask=headbase)
        
        if frames.headaccent_frames:
            headaccent = Image.open(frames.headaccent_frames[n])
            alpha = headaccent.getchannel('A')
            headaccent = Image.new('RGBA', headaccent.size, color=solid_color)
            headaccent.putalpha(alpha)
            frame.paste(headaccent, box=(20, 70), mask=headaccent)

        if frames.headpattern_frames:
            headpattern = Image.open(frames.headpattern_frames[n])
            alpha = headpattern.getchannel('A')
            headpattern = Image.new('RGBA', headpattern.size, color=solid_color)
            headpattern.putalpha(alpha)
            frame.paste(headpattern, box=(20, 70), mask=headpattern)

        if frames.mouth_frames:
            mouth = Image.open(frames.mouth_frames[n])
            alpha = mouth.getchannel('A')
            mouth = Image.new('RGBA', mouth.size, color=solid_color)
            mouth.putalpha(alpha)
            frame.paste(mouth, box=(20, 70), mask=mouth)

        if frames.horns_frames:
            horns = Image.open(frames.horns_frames[n])
            alpha = horns.getchannel('A')
            horns = Image.new('RGBA', horns.size, color=solid_color)
            horns.putalpha(alpha)
            frame.paste(horns, box=(20, 70), mask=horns)
        
        if frames.eyes_frames:
            eyes = Image.open(frames.eyes_frames[n])
            alpha = eyes.getchannel('A')
            eyes = Image.new('RGBA', eyes.size, color=solid_color)
            eyes.putalpha(alpha)
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

    