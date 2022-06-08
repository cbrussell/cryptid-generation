import hashlib
import os
from pathlib import Path
import numpy as np
from tabulate import tabulate
import fnmatch
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = Path(__file__).resolve().parents[1] / "output/stills/"
image_list = fnmatch.filter(os.listdir(image_path), '*_solid.png')
image_count = len(image_list)
shift_value = 0

combined_hash_string = ""
table = []


for i in range(1, (image_count + 1)):
    new_path = image_path / f"{i}_solid.png"
    f = open(new_path, "rb")
    bytes = f.read()
    readable_hash = hashlib.sha256(bytes).hexdigest()
    combined_hash_string += readable_hash
    table.append([i, i, readable_hash])

print(f"The combined hash string is: {combined_hash_string}. \n")

cryptid_array = np.array(table)
provenance_hash = hashlib.sha256(combined_hash_string.encode('utf-8')).hexdigest()


column_values = ["Init", "Shifted", "Hash"]
df =pd.DataFrame(data=cryptid_array, columns=column_values)
df['Shifted'] = np.roll(df['Shifted'], shift = shift_value)
shifted_table = tabulate(df, column_values, tablefmt="fancy_grid", showindex=False)

# output
print(f"Final shifted table is: \n{shifted_table} \n")
print(f"The final provenance hash is {provenance_hash}. \n")
print(f"\nThe shift amount is: {shift_value}.\n")
