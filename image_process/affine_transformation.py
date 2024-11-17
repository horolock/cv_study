import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read color image
image_path = "./content/like_lenna.png"
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# plt.imshow(img)
# plt.title("Original Image")
# plt.show()

def rotate_image(image, angle, center=None):
    rows, cols, _ = image.shape
    if center is None:
        center = (cols // 2, rows // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    rotated = cv2.warpAffine(image, M, (cols, rows))
    return rotated

rotated_image = rotate_image(img, 45)
plt.imshow(rotated_image)
plt.title("Rotated Image")
plt.show()