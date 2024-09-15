#Author: Stan Yin
#GitHub Name: SomeB1oody
#This project is based on CC 4.0 BY, please mention my name if you use it.
#This project requires opencv.

import cv2 as cv

print("Please enter the path of image\t")
print("Example:C:\\Wallpaper\\02.png\t")
path = input("Enter here: ")
image = cv.imread(path, cv.IMREAD_COLOR)

if image is None:
    raise ValueError("Cannot load the image")

alpha = 100
beta = 100

global output_image

def adjustment(input_image, _alpha, _beta):
    print("\t----------------------------------------------------\t")
    print("adjusting\t")
    assert _alpha >= 0, "alpha must be greater than zero"
    global output_image
    output_image = cv.convertScaleAbs(input_image, alpha=_alpha, beta=_beta)
    print("adjust successfully")
    cv.imshow("Brightness and Contrast", output_image)

def alpha_track_bar(alpha_):
    print("\t----------------------------------------------------\t")
    print("alpha adjustment detected\t")
    print("invoking adjustment function\t")
    actual_alpha_value = alpha_ / 100.0
    actual_beta_value = beta -100
    adjustment(image, actual_alpha_value, actual_beta_value)

def beta_track_bar(beta_):
    print("\t----------------------------------------------------\t")
    print("beta adjustment detected\t")
    print("invoking adjustment function\t")
    actual_alpha_value = alpha / 100.0
    actual_beta_value = beta_ - 100
    adjustment(image, actual_alpha_value, actual_beta_value)

cv.namedWindow("Brightness and Contrast")
cv.createTrackbar("Contrast (Alpha)", "Brightness and Contrast", alpha, 200, alpha_track_bar)
cv.createTrackbar("Brightness (Beta)", "Brightness and Contrast", beta, 200, beta_track_bar)

alpha_track_bar(100)
beta_track_bar(100)

cv.waitKey()

cv.imwrite("Brightness and Contrast.jpg", output_image)

cv.destroyAllWindows()