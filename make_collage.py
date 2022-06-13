import os
from PIL import Image, ImageFont, ImageDraw
import fnmatch
from pathlib import Path
import math
import random

def gridSize(n):
     
    grid = []
    a = math.sqrt(n)

    if n % a == 0:
        print("Perfect match!")
    
    else:
        while True:

            print("Trying again, not integer..")
            a = math.floor(a)
            if n % a != 0:
                a -= 1
            else: 
                break
    b = n/a

    grid.append(int(b))
    grid.append(int(a))

    print(f'Highest two divisible factors are {int(b)} and {int(a)}')
    return grid

def main():
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.makedirs(f"{dir_path}/output/collage_still", exist_ok=True)

    still_path = Path(__file__).resolve().parents[1] / "cryptid-generation/output/stills/"

    still_list = [ 'solid'] #, 'transparent', 'transparent_pfp', 'solid_pfp']

    for type in still_list:
        
        still_list = fnmatch.filter(os.listdir(still_path), f'*{type}.png')

        name_file = open("deep_names_shuffle.txt", "r")
        data = name_file.read()
        name_list = data.split("\n")
        name_file.close()

        still_count = len(still_list)

        grid = [25, 25] #[x,y]

        # grid = gridSize(still_count)


        image = Image.open(f"{dir_path}/output/stills/1_{type}.png")

        width, height = image.size

        # frame = Image.new('RGBA', (width*grid[0], height*grid[1]))  # random solid
        frame_count = 1
        for collage_number in range(13):
            frame = Image.new('RGBA', (width*grid[0], height*grid[1]))  # random solid
            
            
            for y in range(grid[1]):
                for x in range(grid[0]):
                    try:

                        still = Image.open(f"{dir_path}/output/stills/{frame_count}_{type}.png")
                        frame.paste(still, box=(height * x, height * y))

                        # watermark settings
                        # find texts with "find {/System,}/Library/Fonts -name *ttf"
                        ######

                        # get brightness of frame for font color selection
                        try:
                            r, g, b = still.getpixel((5, 5))
                        except:
                            r, g, b, a = still.getpixel((5, 5))
                        luma = 0.2126 * r + 0.7152 * g + 0.0722 * b

                        name = name_list.pop(0)

                        Width, Height = frame.size 
                        drawn = ImageDraw.Draw(frame) 
                        text = f"{frame_count}, {name}"  
                        font = ImageFont.truetype("Arial Black", 50)
                        textwidth, textheight = drawn.textsize(text, font)
                        if luma < 150:
                            drawn.text((height * x + 30, height * y + 10), text, font=font, fill="white") 
                        else:
                            drawn.text((height * x + 30, height * y + 10), text, font=font, fill="black")

                        #####

                        print(f"Pasted frame #{frame_count}! Only {still_count - frame_count} more frames left to go!")
                        frame_count += 1

                    except:
                        break

            # ***************     paste to color      ***************     

            finished_width, finished_height = frame.size

            # ***************     scale      ***************     

            if grid[0] * width > 7000:

                basewidth = 7000
                resize_scale = (basewidth)/(width*grid[0])
                frame = frame.resize((basewidth, int(float(height*grid[1]) * resize_scale)))

            # ***************     scale      ***************

            print(f"Saving {type} collage...\n")
            print(f"Collage #{collage_number}...\n")
            frame.save(f"{dir_path}/output/collage_still/full_collage_{grid[0]}_x_{grid[1]}_{type}_{collage_number}_new.png", format="png")  
            print(f'Completed {type} collage!')

if __name__ == "__main__":
    main()