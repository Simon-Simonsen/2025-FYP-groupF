from os.path import join
import pandas as pd
import matplotlib.pyplot as plt

from util.img_util import readImageFile, saveImageFile
from util.inpaint_util import removeHair

"""
We could have used the dataloader class' iter method, but  thought the pandas was more intuiative to use and loop through, while still using
SaveImage and ReadImage functions.
"""


#Use pandas to load our csv as dataframe
df = pd.read_csv("result/result.csv")
#Save column as a list, so we can loop through the desired pictures in our directory.
col_array = df["File_ID"].tolist()

j = 0
#Loop through the list
for i in col_array:
    j += 1
    #Load each picture through the directory

    file_path = '/Users/simonbruun-simonsen/Desktop/data/'+ i
    save_dir = './result'



    # read an image file
    img_rgb, img_gray = readImageFile(file_path)

    # apply hair removal
    blackhat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=5, threshold=10)

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
    #plt.show()
    #Change file_name so we can save it as .jpg.
    save_file_name = i.replace(".png", ".jpg")

    # save the output image
    save_file_path = join(save_dir, "output-" + save_file_name)
    saveImageFile(img_out, save_file_path)
