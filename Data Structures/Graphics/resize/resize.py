import cv2
import sys


image = cv2.imread('154202.png')
if image is None:
    print("Image could not be loaded.")
    sys.exit()


print("--- Original Size ---")
img_size = image.shape
print(img_size)


img_height = img_size[0] // 2
img_width = img_size[1] // 2


resized = cv2.resize(image, (img_width, img_height))

print("--- Resized Size ---")
print(resized.shape)

cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('resized_output.png', resized)
print("Saved resized_output.png successfully!")
