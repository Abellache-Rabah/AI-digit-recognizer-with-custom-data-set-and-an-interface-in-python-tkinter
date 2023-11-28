import numpy as np
from PIL import Image
import fnmatch
import csv 
import json
import os

def splitit(input_list):
    return [input_list[i:i + 25] for i in range(0, len(input_list), 25)]


def load_image(file):
    img = Image.open(file)
    img = img.convert('L')
    img_data = np.array(img)
    img_data = np.where(img_data > 220, 255, 0)
    return img_data

images = []
labels = []



dir_path = './digit'
prefixes = ['0', '1', "2", '3', '4', '5', '6', '7', '8', '9' ]

# for filename in os.listdir(dir_path):
#    for prefix in prefixes:
#        if fnmatch.fnmatch(filename, prefix + '*'):
#             images.append(load_image("./digit/" + filename))
#             labels.append(prefix)
    

images.append(load_image("./digit/zero.bmp"))
labels.append(9)





def split():
    sub_images = []
    for image in images:
        for i in range(0, 50, 10):
            for j in range(0, 50, 10):
                sub_image = image[i:i+10, j:j+10]
                #sub_image = np.where(sub_image, 255, 0)
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

print("----------------------- {} ----------------------------------".format(len(counts)))
print(labels)



# data = []
# for i in range(len(labels)):
#     row = [labels[i], counts[i]]
#     data.append(row)

# # Define CSV file columns
# fields = ['Label', 'Vector']

# # Writing to csv file
# with open('data.csv', 'w', newline='') as csvfile:
#     # Create a csv writer object
#     csvwriter = csv.writer(csvfile)
    
#     # Write the column headers
#     csvwriter.writerow(fields)
    
#     # Write the data rows
#     csvwriter.writerows(data)



# data = []

# for i in range(len(labels)):
#     data.append({
#         "label": int(labels[i]),
#         "vector": [int(x) for x in counts[i]]
#     })


# with open('./data.json', 'w') as f:
#     json.dump(data, f)