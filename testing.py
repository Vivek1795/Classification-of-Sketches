# -*- coding: utf-8 -*-
"""prajju_mach4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xkgwdkUoleMZv_vAXoKZFAzO4RE4sr-5

# The Sketchy Guys
Quick Draw - A Google Doodle Recognition Challenge

Read the classes names
"""

# f = open("mini_classes.txt","r")
# #And for reading use
# classes = f.readlines()
# f.close()

# classes = [c.replace('\n','').replace(' ','_') for c in classes]
# print(classes)

"""# Imports"""

import os
import glob
import cv2
import numpy as np
from tensorflow.python.keras import layers
from tensorflow import keras
import tensorflow as tf

#print(len(os.listdir('data')))

"""# Load the Data

Each class contains different number samples of arrays stored as .npy format. Since we have some memory limitations we only load 4000 images per class.
"""

# def load_data(root, vfold_ratio=0.2, max_items_per_class= 4000 ):
#     all_files = glob.glob(os.path.join(root, '*.npy'))

#     #initialize variables
#     x = np.empty([0, 784])
#     y = np.empty([0])
#     class_names = []

#     #load each data file
#     for idx, file in enumerate(all_files):
#         data = np.load(file)
#         data = data[0: max_items_per_class, :]
#         labels = np.full(data.shape[0], idx)

#         x = np.concatenate((x, data), axis=0)
#         y = np.append(y, labels)

#         class_name, ext = os.path.splitext(os.path.basename(file))
#         class_names.append(class_name)

#     data = None
#     labels = None

#     #randomize the dataset
#     permutation = np.random.permutation(y.shape[0])
#     x = x[permutation, :]
#     y = y[permutation]

#     #separate into training and testing
#     vfold_size = int(x.shape[0]/100*(vfold_ratio*100))

#     x_test = x[0:vfold_size, :]
#     y_test = y[0:vfold_size]

#     x_train = x[vfold_size:x.shape[0], :]
#     y_train = y[vfold_size:y.shape[0]]
#     return x_train, y_train, x_test, y_test, class_names

# x_train, y_train, x_test, y_test, class_names = load_data('data')
# num_classes = len(class_names)
# image_size = 28

# print(len(x_train))

"""Show some random data"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
from random import randint
# %matplotlib inline
# idx = randint(0, len(x_train))
# plt.imshow(x_train[idx].reshape(28,28))

# print(class_names[int(y_train[idx].item())])

# """# Preprocess the Data"""

# # Reshape and normalize
# x_train = x_train.reshape(x_train.shape[0], image_size, image_size, 1).astype('float32')
# x_test = x_test.reshape(x_test.shape[0], image_size, image_size, 1).astype('float32')

# x_train /= 255.0
# x_test /= 255.0

# # Convert class vectors to class matrices
# y_train = keras.utils.to_categorical(y_train, num_classes)
# y_test = keras.utils.to_categorical(y_test, num_classes)

# """# The Model

# **MODEL 1**
# """

# Define model
from keras.layers import Convolution2D, MaxPooling2D, LSTM, Dense, Flatten, Dropout, BatchNormalization, Bidirectional


model = keras.Sequential()
model.add(Convolution2D(16, (3, 3),
                        padding='same',
                        input_shape=(28,28,1), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(32, (3, 3),
                        padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, (3, 3),
                        padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(128, (3, 3),
                        padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(100, activation='softmax'))

# Train model
adam = tf.optimizers.Adam()
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['top_k_categorical_accuracy'])
print(model.summary())

model.load_weights('sketchyguys.keras')

"""**Visualize the Training model**"""

from keras.utils import plot_model
#plot_model(model, to_file='conv_model_plot.png', show_shapes=True, show_layer_names=True)

"""# Training"""

#model.fit(x = x_train, y = y_train, validation_split=0.05, batch_size = 64, verbose=2, epochs=100)

#model.load_weights('sketchyguys.keras')

"""# Training Accuracy"""

# score = model.evaluate(x_train, y_train, verbose=0)
# print('Train accuarcy: {:0.2f}%'.format(score[1] * 100))

# """# Test Accuracy"""

# score = model.evaluate(x_test, y_test, verbose=0)
# print('Test accuracy: {:0.2f}%'.format(score[1] * 100))

"""# Inference"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
from random import randint
from PIL import Image
# %matplotlib inline
#idx = randint(0, len(x_test))
#----------------------------GUI--------------------

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image1 = Image.open(file_path)
        image = image.resize((300, 300))  # Resize the image to fit the window
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        label.place(x=(root.winfo_screenwidth() - 300) // 2, y=(root.winfo_screenheight() - 300) // 2)
        
        resized_image = image.resize((28, 28), Image.NEAREST)
        # Convert the image to a numpy array and normalize the pixel values
        image_array = np.array(resized_image)
        # Flatten the image array to match the input shape of your model
        image_flattened = image_array.flatten()
        image_array_squeezed = np.squeeze(image_array)
        plt.imshow(image_array_squeezed)
        #plt.show()
        
        rgb_array = np.array(image_array_squeezed)

        # Convert the RGB array to a grayscale array
        gray_array = np.dot(rgb_array[...,:3], [0.299, 0.587, 0.114])

        # Convert the grayscale array back to a PIL Image
        gray_image = Image.fromarray(gray_array.astype(np.uint8))
        
        #resized_flattened_image = image_flattened.reshape(1, 28, 28, 1)
        # gray_image = cv2.cvtColor(image_array_squeezed, cv2.COLOR_RGB2GRAY)
        
        input_data_reshaped = gray_array.reshape(28, 28, 1)
        plt.imshow(gray_image, cmap='Grays')
        plt.show()
        pred = model.predict(np.expand_dims(input_data_reshaped, axis=0))[0]

        class_names = ['flower', 'mountain', 'car', 'candle', 'clock', 'tennis_racquet', 'helmet', 'airplane', 'shorts', 'rifle', 'face', 'knife', 'diving_board', 'cup', 'moustache', 'spider', 'mushroom', 'bicycle', 'headphones', 'beard', 'key', 'saw', 'traffic_light', 'triangle', 'sun', 'envelope', 'ladder', 'lollipop', 'wristwatch', 'anvil', 'radio', 'umbrella', 'coffee_cup', 'shovel', 'alarm_clock', 'wheel', 'laptop', 'power_outlet', 'fan', 'baseball', 'cookie', 'circle', 'cell_phone', 'baseball_bat', 'ceiling_fan', 'pencil', 'syringe', 'paper_clip', 'chair', 'camera', 'snake', 'line', 'apple', 'star', 'cat', 'broom', 'hat', 'bench', 'suitcase', 'scissors', 'hammer', 'bread', 'frying_pan', 'light_bulb', 'ice_cream', 'microphone', 'table', 'dumbbell', 'axe', 'eye', 'bridge', 'tent', 'square', 'smiley_face', 'sock', 'book', 'moon', 'sword', 'hot_dog', 'eyeglasses', 'drums', 'bed', 'pizza', 'pillow', 'lightning', 't-shirt', 'tooth', 'spoon', 'bird', 'butterfly', 'donut', 'screwdriver', 'basketball', 'cloud', 'pants', 'tree', 'stop_sign', 'door', 'grapes', 'rainbow']


        ind = (-pred).argsort()[:5]
        latex = [class_names[x] for x in ind]
        print("latex =",latex)
        
        
        text_box1 = tk.Entry(root, fg='black')
        text_box1.insert(0, latex[0])
        text_box1.bind('<FocusIn>', on_entry_click1)
        text_box1.bind('<FocusOut>', on_focusout1)
        text_box1.place(relx=0.4, rely=0.73, anchor="center")
        
        # Create a text box
        text_box2 = tk.Entry(root, fg='black')
        text_box2.insert(0, latex[1])
        text_box2.bind('<FocusIn>', on_entry_click2)
        text_box2.bind('<FocusOut>', on_focusout2)
        text_box2.place(relx=0.5, rely=0.73, anchor="center")

        # Create a text box
        text_box3 = tk.Entry(root, fg='black')
        text_box3.insert(0, latex[2])
        text_box3.bind('<FocusIn>', on_entry_click3)
        text_box3.bind('<FocusOut>', on_focusout3)
        text_box3.place(relx=0.6, rely=0.73, anchor="center")

        # """# Store the classes"""

        # with open('class_names.txt', 'w') as file_handler:
        #     for item in class_names:
        #         file_handler.write("{}\n".format(item))
        
        

# Function to exit the application
def exit_app():
    root.destroy()

def on_entry_click1(event):
    if text_box1.get() == 'Prediction 1':
        text_box1.delete(0, "end")  # delete all the text in the entry
        text_box1.insert(0, '')  # insert blank for user input
        text_box1.config(fg = 'black')
def on_entry_click2(event):
    if text_box2.get() == 'Prediction 2':
        text_box2.delete(0, "end")  # delete all the text in the entry
        text_box2.insert(0, '')  # insert blank for user input
        text_box2.config(fg = 'black')
def on_entry_click3(event):
    if text_box3.get() == 'Prediction 3':
        text_box3.delete(0, "end")  # delete all the text in the entry
        text_box3.insert(0, '')  # insert blank for user input
        text_box3.config(fg = 'black')

def on_focusout1(event):
    if text_box1.get() == '':
        text_box1.insert(0, 'Prediction 1')
        text_box1.config(fg = 'grey')
def on_focusout2(event):
    if text_box2.get() == '':
        text_box2.insert(0, 'Prediction 2')
        text_box2.config(fg = 'grey')
def on_focusout3(event):
    if text_box3.get() == '':
        text_box3.insert(0, 'Prediction 3')
        text_box3.config(fg = 'grey')

# Create the main window
root = tk.Tk()
root.title("Image Viewer")

# Set the window size to full screen
root.attributes('-fullscreen', True)

# Load and display background image
background_image = Image.open("background.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Make the background image fill the entire window

# Create a label to display the image
label = tk.Label(root)
label.pack()

# Create a text box
text_box1 = tk.Entry(root, fg='grey')
text_box1.insert(0, 'Prediction 1')
text_box1.bind('<FocusIn>', on_entry_click1)
text_box1.bind('<FocusOut>', on_focusout1)
text_box1.place(relx=0.4, rely=0.73, anchor="center")

# Create a text box
text_box2 = tk.Entry(root, fg='grey')
text_box2.insert(0, 'Prediction 2')
text_box2.bind('<FocusIn>', on_entry_click2)
text_box2.bind('<FocusOut>', on_focusout2)
text_box2.place(relx=0.5, rely=0.73, anchor="center")

# Create a text box
text_box3 = tk.Entry(root, fg='grey')
text_box3.insert(0, 'Prediction 3')
text_box3.bind('<FocusIn>', on_entry_click3)
text_box3.bind('<FocusOut>', on_focusout3)
text_box3.place(relx=0.6, rely=0.73, anchor="center")

# Create an exit button
exit_button = tk.Button(root, text="X", command=exit_app)
exit_button.place(relx=1, x=-10, y=10, anchor="ne")  # Place at top right

# Create a button to open an image
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.place(relx=0.5, rely=0.8, y=-10, anchor="s")  # Place at bottom center

# Run the Tkinter event loop
root.mainloop()




#-------------------------Gui------------------end

