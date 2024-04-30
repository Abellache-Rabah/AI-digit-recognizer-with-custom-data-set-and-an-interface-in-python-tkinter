import tkinter as tk 
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import PIL.Image as PILImage
import numpy as np
import io
import cv2
import numpy as np
import tensorflow as tf
import json
from scipy.spatial.distance import cdist 
from PIL import ImageGrab


from tkinter import messagebox



model = tf.keras.models.load_model('digit_recognizer_tf')


with open('data.json') as f:
    dataset = json.load(f)


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

def reset_coordinates(event):
    global prev_x, prev_y
    prev_x, prev_y = None, None

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

    #compare
    distances = cdist([imageSubMatrix], train_vectors)[0]

#index 
    nearest_idx = np.argmin(distances)

    nearest_label = train_labels[nearest_idx] 
    print("Nearest match label:", nearest_label)
    messagebox.showinfo("Prediction", "The prediction is " + str(index) + " with accuracy " + str(predictions[0][index]) + "\n The Nearist Vector of futuers is : {}".format(nearest_label))

def multiple_number(canvas):
    x,y,width,height = canvas.bbox("all")  # replace your_canvas with your actual canvas name
    image = ImageGrab.grab((x, y, x + width, y + height))

    # Convert the image to a numpy array and then to grayscale
    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # For each contour, calculate the bounding rectangle and draw it on the image
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image_np, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Convert the numpy array image back to PIL image and show it
    image = Image.fromarray(image_np)
    image.show()


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
    canvas.config(width=400, height=400, bg="white", bd=2, relief="solid")


root = tk.Tk() 
# Set the window size
window_width = 500
window_height = 620
root.geometry(f"{window_width}x{window_height}")

# Calculate the position to center the window
position_top = int(root.winfo_screenheight() / 2 - window_height / 2)
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)

# Position the window
root.geometry(f"+{position_right}+{position_top}")


canvas = tk.Canvas(root, width=400, height=400, bg="white", bd=2, relief="solid")
canvas.pack(anchor='center',pady=5)

canvas.bind("<B1-Motion>", draw) 
canvas.bind("<ButtonRelease-1>", reset_coordinates)



buttonClear = tk.Button(root, text="Predect", command=predect , width=40,height=2 , bg="green", fg="white")
buttonClear.pack(pady=5)

buttonPredet = tk.Button(root, text="Predect Multiple Numbers", command=multiple_number , width=40,height=2 , bg="blue", fg="white")
buttonPredet.pack(pady=5)

buttonClear = tk.Button(root, text="Clear", command=clear ,width=40,height=2 , bg="#333", fg="white" )
buttonClear.pack(pady=5)


back_button = tk.Button(root, text="Back", command=root.destroy, bg="red",height=2, fg="white", width=40)
back_button.pack(pady=5)




root.mainloop()