import cv2

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

cv2.imshow("frame", cropped_image)

# End process
cv2.waitKey(0)
cv2.destroyAllWindows()