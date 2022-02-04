import os
import random
from typing import Union

class TraitManifest:
    def __init__(self, manifest):
        self.manifest=manifest

    def attribute(self, attr:str):
        return [x for x in self.manifest if x["attribute"] == attr][0]
    
class ColorManifest:
    def __init__(self, manifest):
        self.manifest = manifest

    def get(self):
        color = random.choices(population=self.manifest, weights=[x["weight"] for x in self.manifest], k=1)[0]
        color = color["color"]
        return color

class BackgroundManifest:
    def __init__(self, manifest):
        self.manifest = manifest

    def get(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        background = random.choices(population=self.manifest, weights=[x["weight"] for x in self.manifest], k=1)[0]
        background = background["color"]
        frame = []
        file_name = f"{dir_path}/RENDERS/0_background/{background}.png"
        frame.append(file_name)
        return background, frame
    
    def get_avoid(self, avoid_list:list):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        background = random.choices(population=[x for x in self.manifest if x["color"] not in avoid_list], weights=[x["weight"] for x in self.manifest if x["color"] not in avoid_list], k=1)[0]
        background = background["color"]
        frame = []
        file_name = f"{dir_path}/RENDERS/0_background/{background}.png"
        frame.append(file_name)
        return background, frame

# [x for x in categories if x["category"] == type]

def chance(rarity):
    return random.random() < rarity

def get_background(color):
    return []

# get random trait, output {attrib: trait} (dict), category (str), color (str), frames (list of strings)
def get_trait(manifest: TraitManifest, attribute: str) -> Union[dict, str, str, list]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    attrib = manifest.attribute(attribute)
    categories = attrib["categories"]
    if chance(attrib["rarity"]):
        category = random.choices(population = categories, weights = [x["weight"] for x in categories], k=1)[0]
        colors = category["colors"]

        # get random color
        color = random.choices(population = colors, weights = [x["weight"] for x in colors], k=1)[0]
        traits = color["traits"]

        # get random trait
        trait = random.choices(population = traits, weights = [x["weight"] for x in traits], k=1)[0]

    else:
        return {}, '', '', []
    data = {}
    data[attribute]=trait['trait']
    name = trait['trait']
    images = []
    for i in range(1, 73):
        file_name = f"{dir_path}/RENDERS/{attribute}/{name}/{name}_{i:03}.png"
        images.append(file_name)
    return data, category['category'], color['color'], images

# given a category, get a random trait (from a random color)
def get_trait_category(manifest: TraitManifest, attribute: str, type: str) -> Union[dict, str, str, list]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    attrib = manifest.attribute(attribute)
    categories = attrib["categories"]
    if chance(attrib["rarity"]):
        if [x["weight"] for x in categories if x["category"] == type][0] == 0:
            # print(f'No weights set for {attribute}/{type}')
            return {}, '', '', []
        else:

            category = random.choices(population = [x for x in categories if x["category"] == type], weights = [x["weight"] for x in categories if x["category"] == type], k=1)[0]
            colors = category["colors"]
            # traits = category["traits"]

             # get random color
            color = random.choices(population = colors, weights = [x["weight"] for x in colors], k=1)[0]
            traits = color["traits"]

            # get random trait
            trait = random.choices(population = traits, weights = [x["weight"] for x in traits], k=1)[0]
    else:
        return {}, '', '', []
    data = {}
    data[attribute]=trait['trait']
    name = trait['trait']
    images = []
    for i in range(1, 73):
        file_name = f"{dir_path}/RENDERS/{attribute}/{name}/{name}_{i:03}.png"
        images.append(file_name)
    return data, category['category'], color['color'], images

# given a category, get a random trait (from a random color)
def get_trait_category_color(manifest: TraitManifest, attribute: str, type: str, base_color: str) -> Union[dict, str, str, list]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    attrib = manifest.attribute(attribute)
    categories = attrib["categories"]
    if chance(attrib["rarity"]):
        if [x["weight"] for x in categories if x["category"] == type][0] == 0:
            # print(f'No weights set for {attribute}/{type}')
            return {}, '', '', []
        else:
            category = random.choices(population = [x for x in categories if x["category"] == type], weights = [x["weight"] for x in categories if x["category"] == type], k=1)[0]
            colors = category["colors"]
            color = random.choices(population = [x for x in colors if x["color"] == base_color], weights = [x["weight"] for x in colors if x["color"] == base_color], k=1)[0]
            traits = color["traits"]
            trait = random.choices(population = traits, weights = [x["weight"] for x in traits], k=1)[0]
    else:
        return {}, '', '', []
    data = {}
    data[attribute]=trait['trait']
    name = trait['trait']
    images = []
    for i in range(1, 73):
        file_name = f"{dir_path}/RENDERS/{attribute}/{name}/{name}_{i:03}.png"
        images.append(file_name)
    return data, category['category'], color['color'], images

# get trait, random category/type, but use input as selected base_color
def get_trait_color(manifest: TraitManifest, attribute: str, base_color: str) -> Union[dict, str, str, list]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    attrib = manifest.attribute(attribute)
    categories = attrib["categories"]
    if chance(attrib["rarity"]):
        category = random.choices(population = categories, weights = [x["weight"] for x in categories], k=1)[0]
        colors = category["colors"]

        # get chosen color
     
        color = random.choices(population = [x for x in colors if x["color"] == base_color], weights = [x["weight"] for x in colors if x["color"] == base_color], k=1)[0]
        traits = color["traits"]

        # get random trait
        trait = random.choices(population = traits, weights = [x["weight"] for x in traits], k=1)[0]

    else:
        return {}, '', '', []
    data = {}
    data[attribute]=trait['trait']
    name = trait['trait']
    images = []
    for i in range(1, 73):
        file_name = f"{dir_path}/RENDERS/{attribute}/{name}/{name}_{i:03}.png"
        images.append(file_name)
    return data, category['category'], color['color'], images  

def get_trait_color_avoid_category(manifest: TraitManifest, attribute: str, base_color: str, avoid_list: list) -> Union[dict, str, str, list]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    attrib = manifest.attribute(attribute)
    categories = attrib["categories"]
    if chance(attrib["rarity"]):
        category = random.choices(population = [x for x in categories if x["category"] not in avoid_list], weights = [x["weight"] for x in categories if x["category"] not in avoid_list], k=1)[0]
        colors = category["colors"]

        # get chosen color
        color = random.choices(population = [x for x in colors if x["color"] == base_color], weights = [x["weight"] for x in colors if x["color"] == base_color], k=1)[0]
        traits = color["traits"]

        # get random trait
        trait = random.choices(population = traits, weights = [x["weight"] for x in traits], k=1)[0]

    else:
        return {}, '', '', []
    data = {}
    data[attribute]=trait['trait']
    name = trait['trait']
    images = []
    for i in range(1, 73):
        file_name = f"{dir_path}/RENDERS/{attribute}/{name}/{name}_{i:03}.png"
        images.append(file_name)
    return data, category['category'], color['color'], images    
