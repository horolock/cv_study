import cv2

image = cv2.imread('like_lenna.png', cv2.IMREAD_GRAYSCALE)

if image is not None:
    print("이미지를 읽어왔습니다.")
else:
    print("이미지를 읽어오지 못했습니다.")

print(f"변수 타입: {type(image)}")

cv2.imshow('frame', image)

image_small = cv2.resize(image, (100, 100))
cv2.imshow('small_image',image_small)


# End process
cv2.waitKey(0)
cv2.destroyAllWindows()