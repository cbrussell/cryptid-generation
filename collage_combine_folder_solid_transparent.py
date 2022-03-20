import os
from PIL import Image, ImageFont, ImageDraw
import fnmatch
from pathlib import Path
from matplotlib import image, scale 
from prime_factor import gridSize


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    still_path = Path(__file__).resolve().parents[1] / "cryptid-generation/output/stills/"

    still_list = fnmatch.filter(os.listdir(still_path), '*transparent.png')

    colors_file = open("deep_names.txt", "r")
    data = colors_file.read()
    colors_list = data.split("\n")
    colors_file.close()

    still_count = len(still_list)

    # grid = [4, 8] #[x,y]

    # print(grid)

    grid = gridSize(still_count)

    # print(grid)

    image = Image.open(f"{dir_path}/output/stills/1_transparent.png")

    width, height = image.size

    frame = Image.new('RGBA', (width*grid[0], height*grid[1]))# random solid

    frame_count = 1
    for y in range(grid[1]):
        for x in range(grid[0]):
            still = Image.open(f"{dir_path}/output/stills/{frame_count}_transparent.png")
            frame.paste(still, box=(height * x, height * y))

                    # watermark settings
            # find texts with "find {/System,}/Library/Fonts -name *ttf"
            ######
    
            Width, Height = frame.size 
            drawn = ImageDraw.Draw(frame) 
            text = f"{frame_count}, {colors_list[frame_count -1 ]}"
            font = ImageFont.truetype("Arial Black", 60)
            textwidth, textheight = drawn.textsize(text, font)
         
         
            
            drawn.text((height * x + 30, height * y + 10), text, font=font, fill="white") 
    
            #####


            print(f"Pasted frame #{frame_count}! Only {still_count - frame_count} more frames left to go!")
            frame_count += 1



    # ***************     paste to color      ***************     


    finished_width, finished_height = frame.size

    # ***************     scale      ***************     

    basewidth = 7000
    resize_scale = (basewidth)/(width*grid[0])
    frame = frame.resize((basewidth, int(float(height*grid[1]) * resize_scale)))

    # ***************     scale      ***************

    print("Saving transparent collage...")
    frame.save(f"{dir_path}/output/collage_still/full_collage_{grid[0]}_x_{grid[1]}_transparent.png", format="png")  
    print(f'Completed Collage!')

  ###### head pfp collage

    still_path = Path(__file__).resolve().parents[1] / "cryptid-generation/output/stills/"

    still_list = fnmatch.filter(os.listdir(still_path), '*transparent_pfp.png')


    still_count = len(still_list)

    # grid = [4, 8] #[x,y]

    # print(grid)

    grid = gridSize(still_count)

    # print(grid)

    image = Image.open(f"{dir_path}/output/stills/1_transparent_pfp.png")

    width, height = image.size

    frame = Image.new('RGBA', (width*grid[0], height*grid[1]))# random solid

    frame_count = 1
    for y in range(grid[1]):
        for x in range(grid[0]):
            still = Image.open(f"{dir_path}/output/stills/{frame_count}_transparent_pfp.png")
            frame.paste(still, box=(height * x, height * y))

                    # watermark settings
            # find texts with "find {/System,}/Library/Fonts -name *ttf"
            ######
    
            Width, Height = frame.size 
            drawn = ImageDraw.Draw(frame) 
            text = f"{frame_count}, {colors_list[frame_count -1 ]}"
            font = ImageFont.truetype("Arial Black", 60)
            textwidth, textheight = drawn.textsize(text, font)
         
            
            drawn.text((height * x + 30, height * y + 10), text, font=font, fill="white") 
    
            #####


            print(f"Pasted frame #{frame_count}! Only {still_count - frame_count} more frames left to go!")
            frame_count += 1



    # ***************     paste to color      ***************     


    finished_width, finished_height = frame.size

    # ***************     scale      ***************     

    basewidth = 7000
    resize_scale = (basewidth)/(width*grid[0])
    frame = frame.resize((basewidth, int(float(height*grid[1]) * resize_scale)))

    # ***************     scale      ***************

    print("Saving solid pfp collage...")
    frame.save(f"{dir_path}/output/collage_still/full_collage_{grid[0]}_x_{grid[1]}_transparent_pfp.png", format="png")  
    print(f'Completed transparent pfp collage!')

    ###
    still_path = Path(__file__).resolve().parents[1] / "cryptid-generation/output/stills/"

    still_list = fnmatch.filter(os.listdir(still_path), '*solid.png')


    still_count = len(still_list)

    # grid = [4, 8] #[x,y]

    # print(grid)

    grid = gridSize(still_count)

    # print(grid)

    image = Image.open(f"{dir_path}/output/stills/1_solid.png")

    width, height = image.size

    frame = Image.new('RGBA', (width*grid[0], height*grid[1]))# random solid

    frame_count = 1
    for y in range(grid[1]):
        for x in range(grid[0]):
            still = Image.open(f"{dir_path}/output/stills/{frame_count}_solid.png")
            frame.paste(still, box=(height * x, height * y))

                    # watermark settings
            # find texts with "find {/System,}/Library/Fonts -name *ttf"
            ######
    
            Width, Height = frame.size 
            drawn = ImageDraw.Draw(frame) 
            text = f"{frame_count}, {colors_list[frame_count -1 ]}"
            font = ImageFont.truetype("Arial Black", 60)
            textwidth, textheight = drawn.textsize(text, font)
         
            
            drawn.text((height * x + 30, height * y + 10), text, font=font, fill="white") 
    
            #####


            print(f"Pasted frame #{frame_count}! Only {still_count - frame_count} more frames left to go!")
            frame_count += 1



    # ***************     paste to color      ***************     


    finished_width, finished_height = frame.size

    # ***************     scale      ***************     

    basewidth = 7000
    resize_scale = (basewidth)/(width*grid[0])
    frame = frame.resize((basewidth, int(float(height*grid[1]) * resize_scale)))

    # ***************     scale      ***************

    print("Saving solid collage...")
    frame.save(f"{dir_path}/output/collage_still/full_collage_{grid[0]}_x_{grid[1]}_solid.png", format="png")  
    print(f'Completed solid collage!')


    ###### head pfp collage

    still_path = Path(__file__).resolve().parents[1] / "cryptid-generation/output/stills/"

    still_list = fnmatch.filter(os.listdir(still_path), '*solid_pfp.png')


    still_count = len(still_list)

    # grid = [4, 8] #[x,y]

    # print(grid)

    grid = gridSize(still_count)

    # print(grid)

    image = Image.open(f"{dir_path}/output/stills/1_solid_pfp.png")

    width, height = image.size

    frame = Image.new('RGBA', (width*grid[0], height*grid[1]))# random solid

    frame_count = 1
    for y in range(grid[1]):
        for x in range(grid[0]):
            still = Image.open(f"{dir_path}/output/stills/{frame_count}_solid_pfp.png")
            frame.paste(still, box=(height * x, height * y))

                    # watermark settings
            # find texts with "find {/System,}/Library/Fonts -name *ttf"
            ######
    
            Width, Height = frame.size 
            drawn = ImageDraw.Draw(frame) 
            text = f"{frame_count}, {colors_list[frame_count -1 ]}"
            font = ImageFont.truetype("Arial Black", 60)
            textwidth, textheight = drawn.textsize(text, font)
         
            
            drawn.text((height * x + 30, height * y + 10), text, font=font, fill="white") 
    
            #####


            print(f"Pasted frame #{frame_count}! Only {still_count - frame_count} more frames left to go!")
            frame_count += 1



    # ***************     paste to color      ***************     


    finished_width, finished_height = frame.size

    # ***************     scale      ***************     

    basewidth = 7000
    resize_scale = (basewidth)/(width*grid[0])
    frame = frame.resize((basewidth, int(float(height*grid[1]) * resize_scale)))

    # ***************     scale      ***************

    print("Saving solid pfp collage...")
    frame.save(f"{dir_path}/output/collage_still/full_collage_{grid[0]}_x_{grid[1]}_solid_pfp.png", format="png")  
    print(f'Completed solid pfp collage!')




if __name__ == "__main__":
    main()
