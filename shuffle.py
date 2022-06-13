import random

name_file = open("deep_names.txt", "r")
data = name_file.read()
name_list = data.split("\n")
name_file.close()

# mylist = ["apple", "banana", "cherry"]
random.shuffle(name_list)

with open("deep_names_shuffle.txt", "w") as fout:
    print(*name_list, sep="\n", file=fout)

