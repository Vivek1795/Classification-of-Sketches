import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read the image
image = cv2.imread('3.jpg')  # Replace 'm.png' with the path to your image

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to highlight black areas
_, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Invert the thresholded image
thresholded_image = cv2.bitwise_not(thresholded_image)

# Resize the image to (128, 128)
resized_image = cv2.resize(thresholded_image, (28, 28))

# Add a single channel dimension
#resized_image = resized_image[:, :, np.newaxis]

# Normalize the image by dividing each value by 255.0
resized_image = resized_image / 255.0