from collections import deque
import os
from pathlib import Path 
import fnmatch
import shutil

shift_amount = 589123

still_path= Path(__file__).resolve().parents[1] / "output/stills/"

shifted_still_path = Path(__file__).resolve().parents[1] / "output/stills_shifted"

image_list = fnmatch.filter(os.listdir(still_path), '*.png')

image_count = len(image_list)

image_list = sorted(image_list, key=lambda x: int(os.path.splitext(x)[0]))

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


