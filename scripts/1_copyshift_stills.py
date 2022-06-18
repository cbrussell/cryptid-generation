from collections import deque
import os
from pathlib import Path 
import fnmatch
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))
os.makedirs(f"{dir_path}/output/stills", exist_ok=True)

shift_amount = 800813

# files = {"_solid.png": "image", "_transparent.png": "image_t", "_solid_pfp.png": "pfp", "_transparent_pfp.png": "pfp_t", "_apng.png": "apng", ".mp4": "mp4", ".gif": "gif", ".json": "metadata"}
files = {".json": "metadata"}

still_path= Path(__file__).resolve().parents[1] / "output/stills/"



for file_type in files:

    shifted_still_path = Path(__file__).resolve().parents[1] / f"output/shifted/{files[file_type]}"
    os.makedirs(f"{shifted_still_path}", exist_ok=True)


    image_list = fnmatch.filter(os.listdir(still_path), f'*{file_type}')

    image_count = len(image_list)

   
    # sort list of files
    image_list.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

    # Rotate list using deque
    test_list = deque(image_list)
    test_list.rotate(shift_amount)
    shifted_list = list(test_list)

    # Output
    print(f"\nOriginal list is: {image_list}\n")
    print(f"\nShifted list is: {shifted_list}\n")

    # Replace original files for new name (changing folders)
    for i in range(image_count):

        new_name = Path(shifted_still_path / shifted_list[i]) #file

        original_name = Path(still_path / image_list[i]) #location

        shutil.copy(original_name, new_name)