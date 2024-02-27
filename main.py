import tkinter as tk
from tkinter import ttk
import os
import time
from tkinter import messagebox


def create_dataset():
    os.system("python createNumbers.py")


def train_ai():
    progress_bar['maximum'] = 100

    os.system("python tensorflow_train.py")

    for i in range(101):
        progress_bar['value'] = i
        root.update_idletasks()
        time.sleep(0.03)  
    messagebox.showinfo("Trained", "Ai is Done Training ")

def test_ai():
    os.system("python interfaace.py")

def extract_features():
    os.system("python cara.py")
    messagebox.showinfo("Extracted", "Extracting Features Done ")


root = tk.Tk()

window_width = 500
window_height = 600
root.geometry(f"{window_width}x{window_height}")

position_top = int(root.winfo_screenheight() / 2 - window_height / 2)
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)

root.geometry(f"+{position_right}+{position_top}")

create_dataset_button = tk.Button(root, text="1 : Create DataSet", command=create_dataset, bg="#339", fg="white", height=2, width=20,font=("Helvetica", 13))
create_dataset_button.pack(pady=20)

extract_features_button = tk.Button(root, text="2 : Extract Features", command=extract_features, bg="#333", fg="white", height=2, width=20, font=("Helvetica", 13))
extract_features_button.pack(pady=20)

train_ai_button = tk.Button(root, text="3 : Train Ai", command=train_ai, bg="#336", fg="white", height=2, width=20,font=("Helvetica", 13))
train_ai_button.pack(pady=20)

progress_bar = ttk.Progressbar(root, length=200)
progress_bar.pack(pady=10)



test_ai_button = tk.Button(root, text="4 : Test Ai", command=test_ai, bg="#334", fg="white", height=2, width=20,font=("Helvetica", 13))
test_ai_button.pack(pady=20)

root.mainloop()