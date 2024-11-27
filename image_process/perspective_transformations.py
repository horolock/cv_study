from matplotlib import pyplot as plt

import cv2
import numpy as np

image_path = "./content/perspective_test.png"

new_source_image = cv2.imread(image_path)

# Source image's corner coordinates
ordered_corners = np.array([
    [57, 630],
    [936, 330],
    [1404, 792],
    [550, 1431]
], dtype='float32')

# np.linalg.norm = Length of vector
ordered_width = int(max(np.linalg.norm(ordered_corners[0] - ordered_corners[1]), 
                        np.linalg.norm(ordered_corners[2] - ordered_corners[3])))

ordered_height = int(max(np.linalg.norm(ordered_corners[0] - ordered_corners[3]),
                         np.linalg.norm(ordered_corners[1] - ordered_corners[2])))

# 변환이 될 꼭짓점 좌표 지정
ordered_rect_corners = np.array([[0, 0], [ordered_width, 0], [ordered_width, ordered_height], [0, ordered_height]], dtype='float32')


# homography matrix calculation
ordered_scan_matrix = cv2.getPerspectiveTransform(ordered_corners, ordered_rect_corners)

ordered_scanned_image = cv2.warpPerspective(new_source_image, ordered_scan_matrix, (ordered_width, ordered_height))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("New Source Image")
plt.imshow(cv2.cvtColor(new_source_image, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)

plt.title("Ordered Scanned Image")
plt.imshow(cv2.cvtColor(ordered_scanned_image, cv2.COLOR_BGR2RGB))
plt.show()