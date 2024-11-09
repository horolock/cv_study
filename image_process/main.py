import keras
import tensorflow as tf
import matplotlib.pyplot as plt

### For downloading image
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# url = "https://cobslab.com/wp-content/uploads/2022/02/ai-009-1.jpg"
# image_path = keras.utils.get_file('C:/Users/hojoon/Developer/cv_study/image_process/content/image.jpg', origin=url)
###

# Raw binary string
image = tf.io.read_file("C:/Users/hojoon/Developer/cv_study/image_process/content/image.jpg")

# decode to 3d tensor
image = tf.image.decode_jpeg(image, channels=3)

plt.imshow(image)
plt.axis('off')
plt.show()

# Sample RGB Image
rgb_image = tf.random.uniform([100, 100, 3], maxval=255, dtype=tf.float32)

plt.imshow(rgb_image)
plt.title("RGB Image")
plt.axis('off')
plt.show()

# Grayscale
grayscale_image = tf.image.rgb_to_grayscale(rgb_image)

print(grayscale_image.shape)

plt.imshow(grayscale_image.numpy().squeeze(), cmap="gray")
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

### Can do grayscale manually
# grayscale = R * 0.299 + G * 0.587 + B * 0.114
# R = rgb_image[0][0][0] * 0.299
# G = rgb_image[0][0][1] * 0.587
# B = rgb_image[0][0][2] * 0.114
# Y = R + G + B

# HSV
hsv_image = tf.image.rgb_to_hsv(rgb_image)
hue_channel = hsv_image[:, :, 0]    # Only Hue channel

plt.imshow(hue_channel, cmap='hsv')
plt.title('Hue channel of HSV Image')
plt.axis('off')
plt.colorbar(label='Hue Value')
plt.show()

# Normalize
print("Normalize...")
normalized_image = rgb_image / 255.0
print(rgb_image[0][0])
print(normalized_image[0][0])

# Standardize (표준화)
mean = tf.reduce_mean(rgb_image)
stddev = tf.math.reduce_std(rgb_image)

print("Standardize...")
standardized_image = (rgb_image - mean) / stddev
print(rgb_image[0][0])
print(standardized_image[0][0])