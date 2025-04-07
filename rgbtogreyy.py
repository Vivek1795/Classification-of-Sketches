import numpy as np
from PIL import Image

# Load the RGB image
image_path = '2.jpg'
rgb_image = Image.open(image_path)

# Convert the RGB image to a NumPy array
rgb_array = np.array(rgb_image)

# Convert the RGB array to a grayscale array
gray_array = np.dot(rgb_array[...,:3], [0.299, 0.587, 0.114])

# Convert the grayscale array back to a PIL Image
gray_image = Image.fromarray(gray_array.astype(np.uint8))

# Save the grayscale image to a file
gray_image.save('gray_image.jpg')
