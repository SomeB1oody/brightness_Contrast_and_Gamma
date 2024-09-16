#Author: Stan Yin
#GitHub Name: SomeB1oody
#This project is based on CC 4.0 BY, please mention my name if you use it.
#This project requires opencv.

import cv2 as cv
import numpy as np

print("Please enter the path of image\t")
print("Example:C:\\Wallpaper\\02.png\t")
path = input("Enter here: ")
image = cv.imread(path, cv.IMREAD_COLOR)

if image is None:
    raise ValueError("Cannot load the image")

global output_image

gamma = 100

def gamma_correction(input_image, _gamma):
    print("\t----------------------------------------------------\t")
    print("correcting\t")
    global output_image
    assert _gamma >= 0, "Gamma value should be non-negative."
    look_up_table = np.zeros((256,), dtype=np.uint8)
    for index in range(256):
        value = np.clip((index / 255.0) ** _gamma * 255.0, 0, 255)
        look_up_table[index] = np.uint8(value)
    output_image = cv.LUT(input_image, look_up_table)
    print("correct successfully")
    cv.imshow("Gamma Correction", output_image)

def gamma_track_bar(gamma_):
    print("\t----------------------------------------------------\t")
    print("gamma correction detected\t")
    print("invoking correction function\t")
    actual_gamma_value = gamma_/100
    gamma_correction(image, actual_gamma_value)

cv.namedWindow("Gamma Correction")

cv.createTrackbar("Gamma value", "Gamma Correction", gamma, 200, gamma_track_bar)

gamma_track_bar(100)

cv.waitKey()

cv.imwrite("Gamma_correction.jpg", output_image)
