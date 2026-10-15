import cv2

image = cv2.imread('154202.png')

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_height = image.shape[0] // 2
image_width = image.shape[1] // 2
image_channels = image.shape[2] // 2

resize = cv2.resize(image, (image_width, image_height))

Grayscale = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', Grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('grayscale_output.png', Grayscale)
cv2.imwrite('resized_output.png', resize)

#terminalで動かす前にpip install opencv-pythonを入力すればopencvがインストールされるので、インストールしてから動かすこと
