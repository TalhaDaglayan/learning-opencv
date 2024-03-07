# resizing
import os
import cv2

img = cv2.imread(os.path.join('.', 'dogs.jpg'))

resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)