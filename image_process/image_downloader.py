import keras
import ssl

# Read image
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://raw.githubusercontent.com/Lilcob/test_colab/main/perspective_test.jpg'
image_path = keras.utils.get_file('C:/Users/hojoon/Developer/cv_study/image_process/content/perspective_test.png', origin=url)
