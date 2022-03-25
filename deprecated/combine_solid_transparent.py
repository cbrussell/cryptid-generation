import os
import numpy as np
import seaborn as sns
from random import choice
from datetime import datetime
from numpy.core.multiarray import array
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from deprecated.background import get_gradient, get_gradient_3d
from dna import Frames
from time import sleep
from background_2d_generator import get_2d_gradient

def combine_attributes(frames: Frames, prefix: str):
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
 

    palettes = ["Accent", "Accent_r", "Blues", "Blues_r", "BrBG", "BrBG_r", "BuGn", "BuGn_r", "BuPu", "BuPu_r", 
 "CMRmap", "CMRmap_r", "Dark2", "Dark2_r", "GnBu", "GnBu_r", "Greens", "Greens_r", "Greys", "Greys_r", "OrRd", 
 "OrRd_r", "Oranges", "Oranges_r", "PRGn", "PRGn_r", "Paired", "Paired_r", "Pastel1", 
 "Pastel1_r", "Pastel2", "Pastel2_r", "PiYG", "PiYG_r", "PuBu", "PuBuGn", "PuBuGn_r", 
 "PuBu_r", "PuOr", "PuOr_r", "PuRd", "PuRd_r", "Purples", "Purples_r", "RdBu", "RdBu_r", 
 "RdGy", "RdGy_r", "RdPu", "RdPu_r", "RdYlBu", "RdYlBu_r", "RdYlGn", "RdYlGn_r", "Reds", 
 "Reds_r", "Set1", "Set1_r", "Set2", "Set2_r", "Set3", "Set3_r", "Spectral", "Spectral_r", 
 "Wistia", "Wistia_r", "YlGn", "YlGnBu", "YlGnBu_r", "YlGn_r", "YlOrBr", "YlOrBr_r", "YlOrRd", 
 "YlOrRd_r", "afmhot", "afmhot_r", "autumn", "autumn_r", "binary", "binary_r", "bone", 
 "bone_r", "brg", "brg_r", "bwr", "bwr_r", "cividis", "cividis_r", "cool", "cool_r", "coolwarm", "coolwarm_r", "copper", "copper_r",
 "cubehelix", "cubehelix_r", "flag", "flag_r", "gist_earth", "gist_earth_r", "gist_gray", "gist_gray_r", "gist_heat", "gist_heat_r", "gist_ncar", "gist_ncar_r",
 "gist_rainbow", "gist_rainbow_r", "gist_stern", "gist_stern_r", "gist_yarg", 
 "gist_yarg_r", "gnuplot", "gnuplot2", "gnuplot2_r", "gnuplot_r", "gray", "gray_r",
 "hot", "hot_r", "hsv", "hsv_r", "icefire", "icefire_r", "inferno", 
 "inferno_r", "magma", "magma_r", "mako", "mako_r", 
 "nipy_spectral", "nipy_spectral_r", "ocean", "ocean_r", "pink", "pink_r",
 "plasma", "plasma_r", "prism", "prism_r", "rainbow", "rainbow_r",
 "rocket", "rocket_r", "seismic", "seismic_r", "spring", "spring_r",
 "summer", "summer_r", "tab10", "tab10_r", "tab20", "tab20_r", "tab20b",
 "tab20b_r", "tab20c", "tab20c_r", "terrain", "terrain_r", "twilight",
 "twilight_r", "twilight_shifted", "twilight_shifted_r", "viridis", "viridis_r", "vlag", "vlag_r", "winter", "winter_r"]



    selected_palette = choice(palettes)
    outFile = open('colors.txt', 'a')
    outFile.write(f'{selected_palette}\n')
    outFile.close()
    print(f'Selected Palette is {selected_palette}')

    pal = sns.color_palette(selected_palette, 7)

    # pal = sns.color_palette('prism_r', 6)
    color_list = pal.as_hex()


    for n in range(0, 1): #0,72

        frame = Image.new('RGBA', (1100, 1100)) # make transparent background
        
        # R = np.random.randint(0, 256)
        # G = np.random.randint(0, 256)
        # B = np.random.randint(0, 256)

        # R1 = np.random.randint(0, 256)
        # G1 = np.random.randint(0, 256)
        # B1 = np.random.randint(0, 256)

        # R2 = np.random.randint(0, 256)
        # G2 = np.random.randint(0, 256)
        # B2 = np.random.randint(0, 256)

        # R3 = np.random.randint(0, 256)
        # G3 = np.random.randint(0, 256)
        # B3 = np.random.randint(0, 256)

        # R4 = np.random.randint(0, 256)
        # G4 = np.random.randint(0, 256)
        # B4 = np.random.randint(0, 256)

        solid_color = choice(color_list)

        shadow_color = choice(color_list)
        color_list.remove(shadow_color)

        pattern_color = choice(color_list)
        color_list.remove(pattern_color)

        accent_color =choice(color_list)
        color_list.remove(accent_color)

        fur_color = choice(color_list)
        color_list.remove(fur_color)


        mouth_color = choice(color_list)
        color_list.remove(mouth_color)


        back_color = choice(color_list)
        color_list.remove(back_color)

        print(color_list)


        # solid_color = (R, G, B)
        # shadow_color = (R1, G1, B1)
        # pattern_color = (R2, G2, B2)
        # accent_color = (R3, G3, B3)
        # fur_color = (R4, G4, B4)


       
        print(f'Generating frame {n}...')
        if frames.tail_frames:
            tail = Image.open(frames.tail_frames[n])

            alpha = tail.getchannel('A')
            tail = Image.new('RGBA', tail.size, color=solid_color)
            tail.putalpha(alpha) 

            frame = Image.alpha_composite(frame, tail)

            # frame = Image. alpha_composite(frame,tail tail)

        if frames.tailpattern_frames:
            # print(frames.tailpattern_frames[n])
            tailpattern = Image.open(frames.tailpattern_frames[n])


            alpha = tailpattern.getchannel('A')
            tailpattern = Image.new('RGBA', tailpattern.size, color=pattern_color)
            tailpattern.putalpha(alpha) 


            frame = Image.alpha_composite(frame, tailpattern)

        if frames.leftbackleg_frames:
            leftbackleg = Image.open(frames.leftbackleg_frames[n])

            alpha = leftbackleg.getchannel('A')
            leftbackleg = Image.new('RGBA', leftbackleg.size, color=solid_color)
            leftbackleg.putalpha(alpha) 

            frame = Image.alpha_composite(frame, leftbackleg)

        if frames.leftbacklegshadow_frames:
            leftbacklegshadow = Image.open(frames.leftbacklegshadow_frames[n])

            alpha = leftbacklegshadow.getchannel('A')
            leftbacklegshadow = Image.new('RGBA', leftbacklegshadow.size, color=shadow_color)
            leftbacklegshadow.putalpha(alpha) 

            frame = Image.alpha_composite(frame, leftbacklegshadow )

        if frames.leftfrontleg_frames[n]:
            leftfrontleg = Image.open(frames.leftfrontleg_frames[n])

            alpha = leftfrontleg.getchannel('A')
            leftfrontleg = Image.new('RGBA', leftfrontleg.size, color=solid_color)
            leftfrontleg.putalpha(alpha) 

            frame = Image.alpha_composite(frame, leftfrontleg)

        if frames.leftfrontlegshadow_frames[n]:
            leftfrontlegshadow = Image.open(frames.leftfrontlegshadow_frames[n])

            alpha = leftfrontlegshadow.getchannel('A')
            leftfrontlegshadow = Image.new('RGBA', leftfrontlegshadow.size, color=shadow_color)
            leftfrontlegshadow.putalpha(alpha) 

            frame = Image.alpha_composite(frame, leftfrontlegshadow )

        if frames.back_frames:
            back = Image.open(frames.back_frames[n])

            alpha = back.getchannel('A')
            back = Image.new('RGBA', back.size, color=back_color)
            back.putalpha(alpha) 

            frame = Image.alpha_composite(frame, back)
       
        if frames.torsobase_frames:
            torsobase = Image.open(frames.torsobase_frames[n])

            alpha = torsobase.getchannel('A')
            torsobase = Image.new('RGBA', torsobase.size, color=solid_color)
            torsobase.putalpha(alpha) 

            frame = Image. alpha_composite(frame, torsobase)

        if frames.torsoaccent_frames:
            torsoaccent = Image.open(frames.torsoaccent_frames[n])
         
            alpha = torsoaccent.getchannel('A')
            torsoaccent = Image.new('RGBA', torsoaccent.size, color=accent_color)
            torsoaccent.putalpha(alpha) 


            frame = Image.alpha_composite(frame, torsoaccent )

        if frames.torsopattern_frames:
            torsopattern = Image.open(frames.torsopattern_frames[n])

            alpha = torsopattern.getchannel('A')
            torsopattern = Image.new('RGBA', torsopattern.size, color=pattern_color)
            torsopattern.putalpha(alpha)

            frame = Image.alpha_composite(frame, torsopattern)

        if frames.neckbase_frames:
            neckbase = Image.open(frames.neckbase_frames[n])

            alpha = neckbase.getchannel('A')
            neckbase = Image.new('RGBA', neckbase.size, color=solid_color)
            neckbase.putalpha(alpha)

            frame = Image.alpha_composite(frame, neckbase)
        
        if frames.neckaccent_frames:
            neckaccent = Image.open(frames.neckaccent_frames[n])

            alpha = neckaccent.getchannel('A')
            neckaccent = Image.new('RGBA', neckaccent.size, color=accent_color)
            neckaccent.putalpha(alpha)

            frame = Image.alpha_composite(frame, neckaccent)

        if frames.neckpattern_frames:
            neckpattern = Image.open(frames.neckpattern_frames[n])

            alpha = neckpattern.getchannel('A')
            neckpattern = Image.new('RGBA', neckpattern.size, color=pattern_color)
            neckpattern.putalpha(alpha)

            frame = Image.alpha_composite(frame, neckpattern)
        
        if frames.neckshadow_frames:
            neckshadow = Image.open(frames.neckshadow_frames[n])

            alpha = neckshadow.getchannel('A')
            neckshadow = Image.new('RGBA', neckshadow.size, color=shadow_color)
            neckshadow.putalpha(alpha)
            frame = Image.alpha_composite(frame, neckshadow)
        
        if frames.neckshadow_teeth_frames:
            neckshadow_teeth = Image.open(frames.neckshadow_teeth_frames[n])

            alpha = neckshadow_teeth.getchannel('A')
            neckshadow_teeth = Image.new('RGBA', neckshadow_teeth.size, color=shadow_color)
            neckshadow_teeth.putalpha(alpha)

            frame = Image.alpha_composite(frame, neckshadow_teeth)

        if frames.fur_frames:
            fur = Image.open(frames.fur_frames[n])


            alpha = fur.getchannel('A')
            fur = Image.new('RGBA', fur.size, color=fur_color)
            fur.putalpha(alpha)


            frame = Image.alpha_composite(frame, fur)

        if frames.furshadow_frames:
            furshadow = Image.open(frames.furshadow_frames[n])

            alpha = furshadow.getchannel('A')
            furshadow = Image.new('RGBA', furshadow.size, color=shadow_color)
            furshadow.putalpha(alpha)

            frame = Image.alpha_composite(frame, furshadow)

        if frames.fur_shadow_teeth_frames:
            fur_shadow_teeth = Image.open(frames.fur_shadow_teeth_frames[n])

            alpha = fur_shadow_teeth.getchannel('A')
            fur_shadow_teeth = Image.new('RGBA', fur_shadow_teeth.size, color=shadow_color)
            fur_shadow_teeth.putalpha(alpha)

            frame = Image. alpha_composite(frame, fur_shadow_teeth)

        if frames.ear_shadow_fur_frames:
            ear_shadow_fur = Image.open(frames.ear_shadow_fur_frames[n])

            alpha = ear_shadow_fur.getchannel('A')
            ear_shadow_fur = Image.new('RGBA', ear_shadow_fur.size, color=shadow_color)
            ear_shadow_fur.putalpha(alpha)

            frame = Image.alpha_composite(frame, ear_shadow_fur)

        if frames.rightbackleg_frames:
            rightbackleg = Image.open(frames.rightbackleg_frames[n])
            alpha = rightbackleg.getchannel('A')
            rightbackleg = Image.new('RGBA', rightbackleg.size, color=solid_color)
            rightbackleg.putalpha(alpha)
            frame = Image.alpha_composite(frame, rightbackleg)

        if frames.rightbackleg_pattern_frames:
            rightbackleg_pattern = Image.open(frames.rightbackleg_pattern_frames[n])

            alpha = rightbackleg_pattern.getchannel('A')
            rightbackleg_pattern = Image.new('RGBA', rightbackleg_pattern.size, color=pattern_color)
            rightbackleg_pattern.putalpha(alpha)

            frame = Image.alpha_composite(frame, rightbackleg_pattern)
        
        if frames.rightfrontleg_frames:
            rightfrontleg = Image.open(frames.rightfrontleg_frames[n])

            alpha = rightfrontleg.getchannel('A')
            rightfrontleg = Image.new('RGBA', rightfrontleg.size, color=solid_color)
            rightfrontleg.putalpha(alpha)
            frame = Image.alpha_composite(frame, rightfrontleg)

        if frames.rightfrontleg_pattern_frames:
            rightfrontleg_pattern = Image.open(frames.rightfrontleg_pattern_frames[n])

            alpha = rightfrontleg_pattern.getchannel('A')
            rightfrontleg_pattern = Image.new('RGBA', rightfrontleg_pattern.size, color=pattern_color)
            rightfrontleg_pattern.putalpha(alpha)

            frame = Image.alpha_composite(frame, rightfrontleg_pattern)
        
        if frames.ears_frames:
            ears = Image.open(frames.ears_frames[n])
            alpha = ears.getchannel('A')
            ears = Image.new('RGBA', ears.size, color=solid_color)
            ears.putalpha(alpha)

            frame = Image.alpha_composite(frame, ears)

        if frames.headbase_frames:
            headbase = Image.open(frames.headbase_frames[n])

            alpha = headbase.getchannel('A')
            headbase = Image.new('RGBA', headbase.size, color=solid_color)
            headbase.putalpha(alpha)

            frame = Image.alpha_composite(frame, headbase)
        
        if frames.headaccent_frames:
            headaccent =Image.open(frames.headaccent_frames[n])
            alpha = headaccent.getchannel('A')
            headaccent = Image.new('RGBA', headaccent.size, color=accent_color)
            headaccent.putalpha(alpha)

            frame = Image.alpha_composite(frame, headaccent)

        if frames.headpattern_frames:
            headpattern = Image.open(frames.headpattern_frames[n])

            alpha = headpattern.getchannel('A')
            headpattern = Image.new('RGBA', headpattern.size, color=pattern_color)
            headpattern.putalpha(alpha)

            frame = Image.alpha_composite(frame, headpattern)

        if frames.mouth_frames:
            mouth = Image.open(frames.mouth_frames[n])

            alpha = mouth.getchannel('A')
            mouth = Image.new('RGBA', mouth.size, color=mouth_color)
            mouth.putalpha(alpha)

            frame = Image.alpha_composite(frame, mouth)

        if frames.horns_frames:
            horns = Image.open(frames.horns_frames[n])

            alpha = horns.getchannel('A')
            horns = Image.new('RGBA', horns.size, color=solid_color)
            horns.putalpha(alpha)

            frame = Image.alpha_composite(frame, horns)
        
        if frames.eyes_frames:
            eyes = Image.open(frames.eyes_frames[n])
            # alpha = eyes.getchannel('A')
            # eyes = Image.new('RGBA', eyes.size, color=solid_color)
            # eyes.putalpha(alpha)
            frame = Image.alpha_composite(frame, eyes)

        if n == 0:
            # time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            frame.save(f"{dir_path}/output/stills/{prefix}_transparent.png")


        background = Image.open(frames.background_frame[0]) # use chosen background from DNA



        # background = Image.new('RGB', (1180, 1180), (255,245,225)) # supertan)


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

      

        frame = frame.convert("RGBA")  

        background.save(f"{dir_path}/output/raw/{prefix}/{prefix}_{n:03}.png", format="png") 

        if n == 0:
            # time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            background.save(f"{dir_path}/output/stills/{prefix}_solid.png")


            # frame = Image.fromarray(np.uint8(array)).rotate(270).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R1}_{G1}_{B1}_{R}_{G}_{B}.png", "PNG")
           
            # frame = Image.new('RGB', (1180, 1180), (R, G, B)).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R}_{G}_{B}.png", "PNG")
           
            # frame = Image.fromarray(np.uint8(array)).save(f"{dir_path}/output/bg/{prefix}_bg_{time}_{R1}_{G1}_{B1}_{R}_{G}_{B}.png", "PNG")

    