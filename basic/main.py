import cv2
import numpy as np

image = cv2.imread('like_lenna.png', cv2.IMREAD_GRAYSCALE)

if image is not None:
    print("이미지를 읽어왔습니다.")
else:
    print("이미지를 읽어오지 못했습니다.")

print(f"변수 타입: {type(image)}")

cv2.imshow('frame', image)

# 사이즈 변환
image_small = cv2.resize(image, (100, 100))
image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

# 대칭 변환
image_flipped = cv2.flip(image, 0)  # 0 : 수평축 반전, 1 : 세로축 반전

# 회전 변환
height, width = image.shape
matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 30.0, 1.0)
result = cv2.warpAffine(image, matrix, (width, height))

# 자르기
sliced_image = image[50:150, 50:150]

# 원본이 변함
# cropped_image = image[50:150, 50:150]
# cropped_image[:] = 200

# 깊은 복사 기능
cropped_image = image[50:150, 50:150].copy()
cropped_image[:] = 200

# cv2.imshow("frame", cropped_image)

# Draw line
space = np.zeros((500, 1000), dtype=np.uint8)
line_color = 255
space = cv2.line(space, (100, 100), (800, 400), line_color, 3, 1)

# Draw circle
circle_color = 255
space = cv2.circle(space, (600, 200), 100, circle_color, 4, 1)

# Draw rectangle
space = cv2.rectangle(space, (500, 200), (800, 400), line_color, 5, 1)

# Draw ellipse
space = cv2.ellipse(space, (500, 300), (300, 200), 0, 90, 250, line_color, 4)

# cv2.imshow('frame', space)

# 다각형 그리기
space2 = np.zeros((768, 1388), dtype=np.uint8)
color = 255
obj1 = np.array([
    [300, 500], [500, 500], [400, 600], [200, 600]
])

obj2 = np.array([
    [600, 500], [800, 500], [700, 200]
])

space2 = cv2.polylines(space2, [obj1], True, color, 3)
space2 = cv2.fillPoly(space2, [obj2], color, 1)

cv2.imshow('frame', space2)

# End process
cv2.waitKey(0)
cv2.destroyAllWindows()