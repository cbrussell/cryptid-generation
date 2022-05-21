import os
import numpy as np
import sys
import fnmatch
from datetime import datetime
from blend_modes import multiply
from PIL import Image
from pathlib import Path
from multiprocessing import Process, Manager

def main():
   
    jobs = []
    with Manager() as manager:
        color_opacity = {'black': ['#121A24', 0.4] ,'blue': ['#0257A5', 0.2], 'brown': ['#813513', 0.2], 'gray': ['#3E4C5E', 0.2], 'orange': ['#E24211', 0.2], 'purple': ['#3E2566', 0.4], 'red': ['#85000A', 0.2], 'white': ['#FDF7F2', 0.10], 'yellow': ['#Dc7F12', 0.2]}
        start_time = datetime.now()
        for color in color_opacity:
            for stripe_color in color_opacity:
                combined_path = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune_{color}_stripes_{stripe_color}/"
                os.makedirs(combined_path, exist_ok=True)
                process = Process(target=worker_combine, args=(color, stripe_color, combined_path))
                jobs.append(process)
        [j.start() for j in jobs]
        [j.join() for j in jobs]

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f'Completed in {elapsed_time}.')

    return

def worker_combine(color, stripe_color, combined_path):

    os.makedirs(combined_path, exist_ok=True)
    for i in range(1, 73):
        print(f'Making frame {i} for {color}.')

        base_tail_5 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune5/tail_kitsune5_{color}/"
        base_tail_4 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune4/tail_kitsune4_{color}/"
        base_tail_3 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune3/tail_kitsune3_{color}/"
        base_tail_2 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune2/tail_kitsune2_{color}/"
        base_tail_1 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tail_kitsune1/tail_kitsune1_{color}/"

        base_stripe_5 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tailpattern_stripes_kitsune5/tailpattern_stripes_kitsune5_{stripe_color}/"
        base_stripe_4 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tailpattern_stripes_kitsune4/tailpattern_stripes_kitsune4_{stripe_color}/"
        base_stripe_3 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tailpattern_stripes_kitsune3/tailpattern_stripes_kitsune3_{stripe_color}/"
        base_stripe_2 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tailpattern_stripes_kitsune2/tailpattern_stripes_kitsune2_{stripe_color}/"
        base_stripe_1 = Path(__file__).resolve().parents[1] / f"cryptid-generation/output/to_be_combined/tailpattern_stripes_kitsune1/tailpattern_stripes_kitsune1_{stripe_color}/"


        tail_layer_5 = Image.open(base_tail_5 / f'tail_kitsune5_{color}_{i:03}.png')
        tail_layer_4 = Image.open(base_tail_4 / f'tail_kitsune4_{color}_{i:03}.png')
        tail_layer_3 = Image.open(base_tail_3 / f'tail_kitsune3_{color}_{i:03}.png')
        tail_layer_2 = Image.open(base_tail_2 / f'tail_kitsune2_{color}_{i:03}.png')
        tail_layer_1 = Image.open(base_tail_1 / f'tail_kitsune1_{color}_{i:03}.png')

        tail_stripe_5 = Image.open(base_stripe_5 / f'tailpattern_stripes_kitsune5_{stripe_color}_{i:03}.png')
        tail_stripe_4 = Image.open(base_stripe_4 / f'tailpattern_stripes_kitsune4_{stripe_color}_{i:03}.png')
        tail_stripe_3 = Image.open(base_stripe_3 / f'tailpattern_stripes_kitsune3_{stripe_color}_{i:03}.png')
        tail_stripe_2 = Image.open(base_stripe_2 / f'tailpattern_stripes_kitsune2_{stripe_color}_{i:03}.png')
        tail_stripe_1 = Image.open(base_stripe_1 / f'tailpattern_stripes_kitsune1_{stripe_color}_{i:03}.png')

        tail_5_combined = Image.alpha_composite(tail_layer_5, tail_stripe_5)
        tail_4_combined = Image.alpha_composite(tail_layer_4, tail_stripe_4)
        tail_3_combined = Image.alpha_composite(tail_layer_3, tail_stripe_3)
        tail_2_combined = Image.alpha_composite(tail_layer_2, tail_stripe_2)
        tail_1_combined = Image.alpha_composite(tail_layer_1, tail_stripe_1)

        com1 = Image.alpha_composite(tail_5_combined, tail_4_combined)
        com2 = Image.alpha_composite(com1, tail_3_combined)
        com3 = Image.alpha_composite(com2, tail_2_combined)
        com4 = Image.alpha_composite(com3, tail_1_combined)

        com4.save(combined_path / f'tail_kitsune_{color}_stripes_{stripe_color}_{i:03}.png', format="png")

    print(f'Multiprocess job complete! Process ID is {os.getpid()}.')

if __name__ == "__main__":
    main()