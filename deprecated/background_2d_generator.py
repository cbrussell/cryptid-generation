import numpy as np
from PIL import Image, ImageFilter

def get_vertical_gradient(h, w, colourA, colourB): 
    # Make output image
    gradient = np.zeros((h,w,3), np.uint8)

    # Fill R, G and B channels with linear gradient between two end colours
    gradient[:,:,0] = np.linspace(colourA[0], colourB[0], w, dtype=np.uint8)
    gradient[:,:,1] = np.linspace(colourA[1], colourB[1], w, dtype=np.uint8)
    gradient[:,:,2] = np.linspace(colourA[2], colourB[2], w, dtype=np.uint8)

    return gradient

def main():
    R = np.random.randint(0, 256)
    G = np.random.randint(0, 256)
    B = np.random.randint(0, 256)

    R1 = np.random.randint(0, 256)
    G1 = np.random.randint(0, 256)
    B1 = np.random.randint(0, 256)


    # colourA=[5, 2, 2]
    # colourB=[5, 71, 130]

    # colourA=[R, G, B]
    # colourB=[R1, G1, B1]

    colourA=[0, 0, 0]
    colourB=[0, 0, 0]

    h, w = 1100, 1100

    array = get_vertical_gradient(h, w, colourA, colourB)
    
    # frame = Image.fromarray(np.uint8(array))

    background = Image.fromarray(np.uint8(array)).rotate(270)

    # background.filter(ImageFilter.SMOOTH_MORE).show()
    # background.show() 
    background.save("black.png", compress_level=0)

def get_2d_gradient(R, G, B, R1, G1, B1):

    R = np.random.randint(0, 256)
    G = np.random.randint(0, 256)
    B = np.random.randint(0, 256)

    R1 = np.random.randint(0, 256)
    G1 = np.random.randint(0, 256)
    B1 = np.random.randint(0, 256)


    # colourA=[5, 2, 2]
    # colourB=[5, 71, 130]

    colourA=[R, G, B]
    colourB=[R1, G1, B1]


    h, w = 1100, 1100

    gradient = np.zeros((h,w,3), np.uint8)

    # Fill R, G and B channels with linear gradient between two end colours
    gradient[:,:,0] = np.linspace(colourA[0], colourB[0], w, dtype=np.uint8)
    gradient[:,:,1] = np.linspace(colourA[1], colourB[1], w, dtype=np.uint8)
    gradient[:,:,2] = np.linspace(colourA[2], colourB[2], w, dtype=np.uint8)

    # array = get_vertical_gradient(h, w, colourA, colourB)

    return gradient

if __name__ == "__main__":
    main()
