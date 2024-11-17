import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread('./content/like_lenna.png', cv2.IMREAD_GRAYSCALE)

# Create random noise for gaussian filter
mean = 0
sigma = 1

gaussian_noise = np.random.normal(mean, sigma, image.shape).astype('uint8')
noisy_image = cv2.add(image, gaussian_noise)

# plt.imshow(noisy_image, cmap='gray')
# plt.title('Noisy Image')
# plt.axis('off')
# plt.show()

# Using gaussian filter
sigma_values = [1, 5, 10]
denoised_images = []

for sigma in sigma_values:
    denoised = cv2.GaussianBlur(noisy_image, (0, 0), sigma)
    denoised_images.append(denoised)

fig, axes = plt.subplots(1, 4, figsize=(20, 10))

axes[0].imshow(noisy_image, cmap='gray')
axes[0].set_title('Noisy Image')
axes[0].axis('off')

for ax, img, sigma in zip(axes[1:], denoised_images, sigma_values):
    ax.imshow(img, cmap='gray')
    ax.set_title(f'Denoised (o={sigma})')
    ax.axis('off')

plt.tight_layout()
plt.show()