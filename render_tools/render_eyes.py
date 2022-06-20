import os
import sys
import fnmatch
from datetime import datetime
from PIL import Image
from pathlib import Path
from multiprocessing import Process, Manager

def main():
   
    jobs = []
    with Manager() as manager:
        eye_colors = {'red': '#DC0017', 'orange': '#FF8B0E', 'yellow': '#F5B722', 'green': '#18BB55', 'blue': '#0196C7', 'purple': '#8548F7', 'pink': '#EE2893', 'brown': '#C35824', 'gray':  '#7C92A2', 'white': '#E9D2C6'}
        list = ['eyes_beast_iris_left', 'eyes_wise_iris_left', 'eyes_predator_iris_left', 'eyes_goat_iris_left','eyes_beast_iris_right', 'eyes_wise_iris_right', 'eyes_predator_iris_right', 'eyes_goat_iris_right']
        start_time = datetime.now()
        for item in list:
            for color in eye_colors:

                base_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/{item}/"
                combined_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/{item}_final/"

                # count number of pngs
                base_list = fnmatch.filter(os.listdir(base_path), '*.png')
               
                base_frame_count = len(base_list)
                if base_frame_count != 72:
                    sys.exit("Not enough eye frames in file")  

                os.makedirs(combined_path, exist_ok=True)
                
                process = Process(target=worker, args=(color, combined_path, eye_colors, base_path, item))
                jobs.append(process)
        [j.start() for j in jobs]
        [j.join() for j in jobs]

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f'Completed in {elapsed_time}.')

    return

def worker(color, combined_path, eye_colors, base_path, item):
    
    # new folder for each color
    color_path = combined_path / f'{item}_{color}'

    os.makedirs(color_path, exist_ok=True)
    for i in range(1, 73):
        print(f'Making frame {i} for {color}.')
        eyes = Image.open(base_path / f'{item}_{i:03}.png')
        alpha = eyes.getchannel('A')

        # give frame color
        eyes = Image.new('RGBA', eyes.size, color=eye_colors[color])
        eyes.putalpha(alpha)
        eyes.save(color_path / f'{item}_{color}_{i:03}.png', format="png")

    print(f'Multiprocess job complete! Process ID is {os.getpid()}.')

if __name__ == "__main__":
    main()