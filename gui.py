import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image = image.resize((300, 300))  # Resize the image to fit the window
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        label.place(x=(root.winfo_screenwidth() - 300) // 2, y=(root.winfo_screenheight() - 300) // 2)

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
