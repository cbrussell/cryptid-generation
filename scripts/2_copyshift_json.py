from collections import deque
import os
from pathlib import Path 
import fnmatch
import shutil

# Determine image path
json_path = Path(__file__).resolve().parents[1] / "output/metadata/"
new_path = Path(__file__).resolve().parents[1] / "output/metadata_shifted/"

# Renames image directory based on community generated shift-value
shift_amount = 589123
json_list = fnmatch.filter(os.listdir(json_path), '*.json')
sorted_json_list = sorted(json_list, key=lambda x: int(os.path.splitext(x)[0]))
json_count = len(sorted_json_list)

# Rotate list using deque
deque_sorted_json_list = deque(sorted_json_list)
deque_sorted_json_list.rotate(shift_amount)
rotated_deque = list(deque_sorted_json_list)

print(f"\nOriginal list is: {sorted_json_list}\n")
print(f"\nShifted list is: {rotated_deque}\n")
print(f"\nShift amount is: {shift_amount}\n")

# Replace original files for new name (changing folders)
for i in range(json_count):
    new_name = Path(new_path / rotated_deque[i]) #file
    original_name = Path(json_path / sorted_json_list[i]) #location
    shutil.copy(original_name, new_name)