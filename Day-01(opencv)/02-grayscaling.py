'''
Image to grayscale

'''


import cv2
import numpy as np
from matplotlib import pyplot as plt


def imshow(title = "Image", image = None, size = 10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

image = cv2.imread('./data/hioryyyy.jpg')
imshow("hiory_fem", image, size = 7)

#0 is black and 255 is white
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imshow("hiory_fem", gray_image, size = 7)




print(image.shape)
print(gray_image.shape)