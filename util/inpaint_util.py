import cv2
import matplotlib.pyplot as plt
#Threshold increases intensity
#kernel size might increase or decrese blurryness
#radius increases the inpainting
def removeHair(img_org, img_gray, kernel_size=100, threshold=12, radius=3):
    # kernel for the morphological filtering
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))

    # perform the blackHat filtering on the grayscale image to find the hair countours
  

    blackhat = cv2.morphologyEx(img_gray, cv2.MORPH_BLACKHAT, kernel)

    # intensify the hair countours in preparation for the inpainting algorithm

    _, thresh = cv2.threshold(blackhat, threshold, 255, cv2.THRESH_BINARY)

    # inpaint the original image depending on the mask
    img_out = cv2.inpaint(img_org, thresh, radius, cv2.INPAINT_TELEA)

    return blackhat, thresh, img_out    


    # read image as an 8-bit array
image_path = r"C:\Users\Simon\Desktop\groupF project\Assignment-GROUPF\data\example.jpg"
img_bgr = cv2.imread(image_path)

# Check if the image is loaded correctly
if img_bgr is None:
    print("Error: Image not found. Check the file path.")
else:
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    
    blackhat, thresh, img_out = removeHair(img_rgb, img_gray)
    

    
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(blackhat, cmap="gray")
    plt.title("Blackhat Filtered")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(thresh, cmap="gray")
    plt.title("Thresholded Hair Mask")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(img_out)
    plt.title("Final Image (Hair Removed)")
    plt.axis("off")

    plt.show()
