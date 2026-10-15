import cv2
import numpy

image = cv2.imread('154202.png')

image = cv2.rectangle(image,(10,10),(100,200),(0,255,0),-1)
image = cv2.rectangle(image,(100,10),(200,200),(0,200,0),-1)
image = cv2.rectangle(image,(200,10),(300,200),(0,145,0),-1)
image = cv2.rectangle(image,(300,10),(400,200),(0,95,0),-1)
image = cv2.rectangle(image,(400,10),(500,200),(0,0,0),-1)
image = cv2.rectangle(image,(500,10),(600,200),(0,0,95),-1)
image = cv2.rectangle(image,(600,10),(700,200),(0,0,145),-1)
image = cv2.rectangle(image,(700,10),(800,200),(0,0,200),-1)
image = cv2.rectangle(image,(800,10),(900,200),(0,0,255),-1)

cv2.imshow('Image with Rectangles.', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Gradient_Square.png', image)