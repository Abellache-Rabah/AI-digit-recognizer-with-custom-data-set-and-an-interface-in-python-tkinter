import tkinter as tk 
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import numpy as np
import io
import os

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
    
def reset_prev_coordinates(event):
    global prev_x, prev_y
    prev_x, prev_y = None, None


def canvas_to_image(canvas):
    img = Image.open(io.BytesIO(canvas.postscript(colormode='color').encode('utf-8')))
    img  = img.convert("L")
    return img

def image_to_array(img):
    return np.array(img)

def array_to_image(array):
    return Image.fromarray(array)


def draw_image_on_canvas(canvas, img):
    canvas.delete("all")
    width, height = img.size    
    canvas.config(width=width, height=height)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo
    

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



def elimini():
    img = canvas_to_image(canvas)
    array = image_to_array(img)
    img = remove_white_rows_and_columns(array)
    draw_image_on_canvas(canvas, img)
    return img


def SavePic():
    name = inputtxt.get()
    img = canvas_to_image(canvas);
    array = image_to_array(img)
    img = remove_white_rows_and_columns(array)
    img_resized = img.resize((50, 50), Image.LANCZOS)  
    if(name == "test"):
        parent_folder = os.path.dirname(os.getcwd())
        print(parent_folder)
        img_resized.save(os.path.join(parent_folder + "\\trained\\", "test.bmp"), 'bmp')

    else:
        parent_folder = os.path.dirname(os.getcwd())
        print(parent_folder)
        img_resized.save(os.path.join(parent_folder + "\\trained\\digit" , "{}.bmp".format(name)), 'bmp')
        

    clear()

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
window_height = 600
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

inputtxt = tk.Entry(root, width=50) 
inputtxt.pack(pady=5) 

sava = tk.Button(root, text="Save Picture with 50x50", command=SavePic, width=40,height=2 , bg="green", fg="white")
sava.pack(pady=5)

buttonClear = tk.Button(root, text="Clear", command=clear, width=40 ,height=2, bg="#333" , fg="white")
buttonClear.pack(pady=5)

back_button = tk.Button(root, text="Back", command=root.destroy, bg="red",height=2, fg="white", width=40)
back_button.pack(pady=5)

root.mainloop()

root.mainloop()