import numpy as np
from PIL import Image


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

def main():
    R = np.random.randint(0, 256)
    G = np.random.randint(0, 256)
    B = np.random.randint(0, 256)

    R1 = np.random.randint(0, 256)
    G1 = np.random.randint(0, 256)
    B1 = np.random.randint(0, 256)

    array = get_gradient_3d(1100, 1100, (253, 39, 182), (25, 73, 230), (True, False, False))

    background = Image.fromarray(np.uint8(array)) #.rotate(270)
    # background.show() 
    background.save("pinkv2.png")

if __name__ == "__main__":
    main()
