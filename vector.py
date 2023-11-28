import numpy as np
from PIL import Image


def splitit(input_list):
    return [input_list[i:i + 25] for i in range(0, len(input_list), 25)]


def load_image(file):
    img = Image.open(file)
    img = img.convert('L')
    img_data = np.array(img)
    img_data = np.where(img_data > 220, 255, 0)
    return img_data

images = []
images.append(load_image("./test.bmp"))

def split():
    sub_images = []
    for image in images:
        for i in range(0, 50, 10):
            for j in range(0, 50, 10):
                sub_image = image[i:i+10, j:j+10]
                sub_images.append(sub_image)
    return sub_images


    
def count(sub_images):
    n = []
    for matrix in sub_images:
        count = np.sum(matrix < 255)
        n.append(count)
    return n


sub = split()
print("----------------------- Le Vectour de Caraktirizike -----------------------")
counts = count(sub)
counts = splitit(counts)
print(counts)
