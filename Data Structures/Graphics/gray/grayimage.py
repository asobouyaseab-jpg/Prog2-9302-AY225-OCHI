import cv2
import sys

image = cv2.imread('154202.png')
if image is None:
    print("Image could not be loaded.")
    sys.exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("--- Grayscale Image Size ---")
print(gray.shape)

cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('gray_output.png', gray)
print("Saved gray_output.png successfully!")
