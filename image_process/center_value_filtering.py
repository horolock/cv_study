import numpy as np
import cv2
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.axes import Axes

### Create salt pepper noise
def generate_salt_noise(image: np.ndarray):
    num_salt = np.ceil(0.05 * image.size)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    salted_image = image.copy()
    salted_image[coords[0], coords[1]] = 255

    return salted_image

def generate_pepper_noise(image: np.ndarray):
    num_pepper = np.ceil(0.05 * image.size)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    pepper_image = image.copy()
    pepper_image[coords[0], coords[1]] = 0

    return pepper_image
###

# Read input image
lenna_image = cv2.imread('./content/like_lenna.png', cv2.IMREAD_GRAYSCALE)

# Create noise image
salted_lenna = generate_salt_noise(lenna_image)
peppered_lenna = generate_pepper_noise(salted_lenna)

# Median blur
filtered_lenna = cv2.medianBlur(peppered_lenna, 5)

fig: Figure
axes = np.ndarray[Axes]

fig, axes = plt.subplots(1, 4, figsize=(20, 6))

# Check output
axes[0].imshow(lenna_image, cmap='gray')
axes[0].set_title('Original lenna image')
axes[0].axis('off')

axes[1].imshow(salted_lenna, cmap='gray')
axes[1].set_title('Salted lenna image')
axes[1].axis('off')

axes[2].imshow(peppered_lenna, cmap='gray')
axes[2].set_title('Salted and Peppered Lenna')
axes[2].axis('off')

axes[3].imshow(filtered_lenna, cmap='gray')
axes[3].set_title('Median Filtered Lenna')
axes[3].axis('off')

plt.tight_layout()
plt.show()