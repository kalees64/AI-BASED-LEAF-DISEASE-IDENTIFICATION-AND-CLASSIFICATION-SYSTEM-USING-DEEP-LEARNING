import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tkinter import messagebox


model1 = load_model("dcnn.h5")
print("success")


my_w = tk.Tk()
my_w.geometry("400x400")
my_w.title('Tomato Leaf Disease Detection system')
my_font1 = ('times', 18, 'bold')


l1 = tk.Label(my_w, text='Give Leaf Images', width=30, font=my_font1)
l1.grid(row=1, column=1)

import os

def upload_file():
    global img
    global filename
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)

    
    if filename:
        
        file_directory = os.path.dirname(filename)
             
        
        desired_directory = r"D:\leaf\test"
        
        
        desired_directory = os.path.normpath(desired_directory)
        file_directory = os.path.normpath(file_directory)
        
       
        if file_directory == desired_directory:
           
            if filename.lower().endswith('.jpg'):
                
                image_obj = Image.open(filename)
                imgs = image_obj.resize((224, 224))  # Resize the image
                img = ImageTk.PhotoImage(imgs)
                b2 = tk.Button(my_w, image=img)
                b2.grid(row=9, column=1, padx=5, pady=5)
                print(filename)
           
        else:
            
            messagebox.showerror("Error", "Please select a file from the Unwanted image.")
    else:
        
        messagebox.showerror("Error", "Please select a file.")



# Button to upload file
b1 = tk.Button(my_w, text='Upload File', width=20, command=upload_file)
b1.grid(row=2, column=1, padx=5, pady=5)

# Function to predict output
def predict():
    global filename
    if filename:
        # Initialize variables
        ft, st, lt, rt, ut = 0, 0, 0, 0, 0
        h = ""
        out = ""
        outv = 5
        
        # Load and preprocess the image
        img = image.load_img(filename, target_size=(224, 224))
        img = image.img_to_array(img, dtype='uint8')
        img = np.expand_dims(img, axis=0)
        
        # Make predictions using the loaded model
        y_pred = np.argmax(model1.predict(img), axis=-1)
        
        # Determine the result based on the predicted class
        if y_pred[0] == 0:
            out = "Result for the given Image: Tomato Yellow Leaf Curl Virus"
            outv = 0
        elif y_pred[0] == 1:
            out = "Result for the given Image: Tomato Mosaic Virus"
            outv = 1
        elif y_pred[0] == 2:
            out = "Result for the given Image: Tomato Leaf Healthy"
            outv = 1
        
        print(out)
        
        # Show result in a messagebox
        messagebox.showinfo("Result", out)
    else:
        # Display error message if no file is uploaded
        messagebox.showerror("Error", "Please upload an image first.")

# Button to predict output
b3 = tk.Button(my_w, text='Predict Output', width=20, command=predict)
b3.grid(row=6, column=1, padx=5, pady=5)

my_w.mainloop()  # Keep the window open
