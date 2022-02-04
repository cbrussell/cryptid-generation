import numpy as np
from PIL import Image

# Define start and end colours and image height and width
def get_gradient(): 
    R = np.random.randint(0, 256)
    G = np.random.randint(0, 256)
    B = np.random.randint(0, 256)

    R1 = np.random.randint(0, 256)
    G1 = np.random.randint(0, 256)
    B1 = np.random.randint(0, 256)


    colourA=[R, G, B]
    colourB=[R1, G1, B1]
    h, w = 1100, 1100

    # Make output image
    gradient = np.zeros((h,w,3), np.uint8)

    # Fill R, G and B channels with linear gradient between two end colours
    gradient[:,:,0] = np.linspace(colourA[0], colourB[0], w, dtype=np.uint8)
    gradient[:,:,1] = np.linspace(colourA[1], colourB[1], w, dtype=np.uint8)
    gradient[:,:,2] = np.linspace(colourA[2], colourB[2], w, dtype=np.uint8)

    return gradient

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T
        
def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=np.float)
    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)
    return result