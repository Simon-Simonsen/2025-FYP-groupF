from os.path import join
import os


import matplotlib.pyplot as plt

from util.img_util_example_solution import readImageFile, saveImageFile
from util.inpaint_util import removeHair

file_path = r"Assignment-GROUPF/data/example.jpg"
save_dir = r'Assignment-GROUPF/result'

# read an image file
img_rgb, img_gray = readImageFile(file_path)

# apply hair removal
blackhat, thresh, img_out = removeHair(img_rgb, img_gray)

# plot the images
plt.figure(figsize=(15, 10))

# original image
plt.subplot(2, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

# blackHat image
plt.subplot(2, 2, 2)
plt.imshow(blackhat, cmap="gray")
plt.title("BlackHat Image")
plt.axis("off")

# thresholded mask
plt.subplot(2, 2, 3)
plt.imshow(thresh, cmap="gray")
plt.title("Thresholded Mask")
plt.axis("off")

# inpainted image
plt.subplot(2, 2, 4)
plt.imshow(img_out)
plt.title("Inpainted Image")
plt.axis("off")

plt.tight_layout()
plt.show()

if not os.path.exists(save_dir):
    os.makedirs(save_dir)  # Create the directory if it doesn't exist


# save the output image
save_file_path = join(save_dir, 'output.jpg')
saveImageFile(img_out, save_file_path)
