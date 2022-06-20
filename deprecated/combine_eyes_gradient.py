import os
import numpy as np
from PIL import Image
from dna import Frames
from collections import deque
import random
from RenderTools.background_2d_generator import get_2d_gradient

def combine_attributes(frames: Frames, prefix: str, frame_count: int):
    R = np.random.randint(0, 256)
    G = np.random.randint(0, 256)
    B = np.random.randint(0, 256)

    R1 = np.random.randint(0, 256)
    G1 = np.random.randint(0, 256)
    B1 = np.random.randint(0, 256)

    R2 = np.random.randint(0, 256)
    G2 = np.random.randint(0, 256)
    B2 = np.random.randint(0, 256)

    iris_color = (R, G, B)

    outFile = open('iris_colors.txt', 'a')
    outFile.write(f'{iris_color}\n')
    outFile.close()

    # generate list of 72 then rotate it from random integer
    dir_path = os.path.dirname(os.path.realpath(__file__))
    shift_amount = random.randint(0, 72)
    deque_list = deque(list(range(72)))
    deque_list.rotate(shift_amount)
    shifted_list = list(deque_list)

    array = get_2d_gradient(R1, G1, B1, R2, G2, B2)
    background_big = Image.fromarray(np.uint8(array)).rotate(135)
   

    background = background_big.crop((500, 500, 1680, 1680))
    background.save(f"{dir_path}/output/bg/{prefix}_bg_{R1}_{G1}_{B1}_{R2}_{G2}_{B2}.png", "PNG")

    for n in range(0, frame_count): #0,72


        # frame = Image.new('RGB', (1180, 1180), (R, G, B)) # random solid

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
        
        if frames.eyes_iris_left_frames:
            eyes_iris_left = Image.open(frames.eyes_iris_left_frames[n])
            
            alpha = eyes_iris_left.getchannel('A')
            eyes_iris_left = Image.new('RGBA', eyes_iris_left.size, color=iris_color)
            eyes_iris_left.putalpha(alpha) 

            frame = Image.alpha_composite(frame, eyes_iris_left)
        
        if frames.eyes_pupil_left_frames:
            eyes_pupil_left = Image.open(frames.eyes_pupil_left_frames[n])
            frame = Image.alpha_composite(frame, eyes_pupil_left)

        if frames.eyes_eyeline_left_frames:
            eyes_eyeline_left = Image.open(frames.eyes_eyeline_left_frames[n])
            frame = Image.alpha_composite(frame, eyes_eyeline_left)

        if frames.eyes_iris_right_frames:
            eyes_iris_right = Image.open(frames.eyes_iris_right_frames[n])
            
            alpha = eyes_iris_right.getchannel('A')
            eyes_iris_right = Image.new('RGBA', eyes_iris_right.size, color=iris_color)
            eyes_iris_right.putalpha(alpha) 

            frame = Image.alpha_composite(frame, eyes_iris_right)
        
        if frames.eyes_pupil_right_frames:
            eyes_pupil_right = Image.open(frames.eyes_pupil_right_frames[n])
            frame = Image.alpha_composite(frame, eyes_pupil_right)

        if frames.eyes_eyeline_right_frames:
            eyes_eyeline_right = Image.open(frames.eyes_eyeline_right_frames[n])
            frame = Image.alpha_composite(frame, eyes_eyeline_right)

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


        # frame.save(f"{dir_path}/output/raw/{prefix}/{prefix}_{shifted_list[n]:03}_t.png", format="png") # shifted
        frame.save(f"{dir_path}/output/raw/{prefix}/{prefix}_{n:03}_t.png", format="png") 


        # background = Image.open(frames.background_frame[0]) # use chosen background from DNA #removing for eyes with random bg

        # background = Image.new('RGBA', (1180, 1180))
        # background = background.crop((40, 40, 1140, 1140))
        # background.paste(frame, box=(20, 70), mask=frame)
        
                
        # all black cryptid
        
        # alpha = frame.getchannel('A')
        # frame = Image.new('RGBA', frame.size, color='black')
        # frame.putalpha(alpha) 
        background.paste(frame, box=(20, 70), mask=frame)

        frame = frame.convert("RGB")  

        # background.save(f"{dir_path}/output/raw/{prefix}/{prefix}_{shifted_list[n]:03}.png", format="png") # shifted
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


            # frame = Image.fromarray(np.uint8(array)).rotate(270).save(f"{dir_path}/output/bg/{prefix}_bg_{R1}_{G1}_{B1}_{R2}_{G2}_{B2}.png", "PNG")
           
            # frame = Image.new('RGB', (1180, 1180), (R, G, B)).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R}_{G}_{B}.png", "PNG")
           
            # frame = Image.fromarray(np.uint8(array)).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R1}_{G1}_{B1}_{R}_{G}_{B}.png", "PNG")
