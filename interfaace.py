import tkinter as tk 
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import PIL.Image as PILImage
import numpy as np
import io
import os
import numpy as np
import tensorflow as tf
import json
from scipy.spatial.distance import cdist  

from tkinter import messagebox



model = tf.keras.models.load_model('digit_recognizer_tf')
# Load dataset 
with open('data.json') as f:
    dataset = json.load(f)
# Extract training vectors
train_vectors = np.array([sample['vector'] for sample in dataset])
train_labels = np.array([sample['label'] for sample in dataset])


prev_x = None
prev_y = None
def draw(event):
    global prev_x, prev_y
    x, y = event.x, event.y
    if prev_x is not None and prev_y is not None:
        canvas.create_line(prev_x, prev_y, x, y, fill="black", width=6)
    prev_x, prev_y = x, y


def canvas_to_image(canvas):
    img = Image.open(io.BytesIO(canvas.postscript(colormode='color').encode('utf-8')))
    img  = img.convert("L")
    return img

def image_to_array(img):
    return np.array(img)

def array_to_image(array):
    return PILImage.fromarray(array)

def predect() :
    img = canvas_to_image(canvas)
    
    img_data = np.array(img)
    removed_white = remove_white_rows_and_columns(img_data)


    img_resized = removed_white.resize((50, 50), PILImage.LANCZOS) 
    
    imageMatrix = np.array(img_resized)  # Convert to numpy array here
    
    imageSubMatrix = count(split(imageMatrix))  # Pass numpy array to split function
    print(imageSubMatrix)
    input_data = np.array([imageSubMatrix])  
    predictions = model.predict(input_data)
    print("The prediction is ")
    index = np.argmax(predictions[0])
    print(index)
    print("acc :" , predictions[0][index])


    # Compute distance to all training vectors
    distances = cdist([imageSubMatrix], train_vectors)[0]

    # Find index of nearest neighbor 
    nearest_idx = np.argmin(distances)

    # Look up label 
    nearest_label = train_labels[nearest_idx] 
    print("Nearest match label:", nearest_label)
    messagebox.showinfo("Prediction", "The prediction is " + str(index) + " with accuracy " + str(predictions[0][index]) + "\n The Nearist Vector of futuers is : {}".format(nearest_label))




def remove_white_rows_and_columns(image_array):
    i = []
    for x in range(len(image_array)):
        for y in range(len(image_array[x])):
            if image_array[x][y] < 255:
                i.append([x,y])
    

    max_x = max(i, key=lambda x: x[0])[0]
    max_y = max(i, key=lambda x: x[1])[1]
    min_x = min(i, key=lambda x: x[0])[0]
    min_y = min(i, key=lambda x: x[1])[1]
    img = array_to_image(image_array).crop((min_y +1 , min_x +1 , max_y+ 1, max_x+1))
    
    return img

def split(imageMatrix):
    sub_images = []
    for i in range(0, 50, 10):
        for j in range(0, 50, 10):
            sub_image = imageMatrix[i:i+10, j:j+10]  # Now slicing will work
            sub_images.append(sub_image)
    return sub_images

def count(sub_images):
    n = []
    for matrix in sub_images:
        count = np.sum(matrix < 255)
        n.append(count)
    return n


def clear():
    canvas.delete("all")
    global prev_x 
    global prev_y 
    prev_x = None
    prev_y = None
    canvas.config(width=500, height=500, bg="white")


root = tk.Tk() 

canvas = tk.Canvas(root, width=500, height=500, bg="white") 
canvas.pack(expand=True, fill="both") 

canvas.bind("<B1-Motion>", draw) 


buttonClear = tk.Button(root, text="Predect", command=predect)
buttonClear.pack()

buttonClear = tk.Button(root, text="Clear", command=clear)
buttonClear.pack()





root.mainloop()