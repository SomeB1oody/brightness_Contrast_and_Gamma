#Author: Stan Yin
#GitHub Name: SomeB1oody
#This project is based on CC 4.0 BY, please mention my name if you use it.
#This project requires opencv.
import cv2 as cv
import numpy as np
#ask for path of image
print("Please enter the path of the image\t")
print("Example: C:\\Wallpaper\\02.jpg\t")
location = input("Enter HERE: ")
original_img = cv.imread(location, cv.IMREAD_COLOR)
#Determine if the read was successful
if original_img is None:
    raise ValueError("Couldn't load the image")
#Setting Variables
global image_bc, image_g

alpha = 100
beta = 100
gamma = 100
#Linear adjustment
def contrast_brightness_adjustment(input_image, _alpha, _beta):
    global image_bc
    print("\t----------------------------------------------------\t")
    print("adjusting\t")
    assert _alpha >= 0, "alpha must be greater than zero"
    output_image = cv.convertScaleAbs(input_image, alpha=_alpha, beta=_beta)
    print("adjust successfully")
    image_bc = output_image
    cv.imshow("Contrast and Brightness (Linear)", image_bc)
#Nonlinear correction
def gamma_correction(input_image, _gamma):
    print("\t----------------------------------------------------\t")
    print("correcting\t")
    global image_g
    assert _gamma >= 0, "Gamma value should be non-negative."
    look_up_table = np.zeros((256,), dtype=np.uint8)
    for index in range(256):
        value = np.clip((index / 255.0) ** _gamma * 255.0, 0, 255)
        look_up_table[index] = np.uint8(value)
    image_g = cv.LUT(input_image, look_up_table)
    print("correct successfully")
    cv.imshow("Gamma (Nonlinear)", image_g)
#seeting callback function
def alpha_track_bar(_alpha):
    print("\t----------------------------------------------------\t")
    print("alpha adjustment detected\t")
    print("invoking adjustment function\t")
    actual_alpha_value = _alpha / 100.0
    actual_beta_value = beta - 100
    contrast_brightness_adjustment(original_img, actual_alpha_value, actual_beta_value)

def beta_track_bar(_beta):
    print("\t----------------------------------------------------\t")
    print("beta adjustment detected\t")
    print("invoking adjustment function\t")
    actual_alpha_value = alpha / 100.0
    actual_beta_value = _beta - 100
    contrast_brightness_adjustment(original_img, actual_alpha_value, actual_beta_value)

def gamma_track_bar(_gamma):
    print("\t----------------------------------------------------\t")
    print("gamma correction detected\t")
    print("invoking correction function\t")
    actual_gamma_value = _gamma / 100.0
    gamma_correction(original_img, actual_gamma_value)
#setting windows
cv.namedWindow("Contrast and Brightness (Linear)", cv.WINDOW_AUTOSIZE)
cv.namedWindow("Gamma (Nonlinear)", cv.WINDOW_AUTOSIZE)
#create track bar
cv.createTrackbar("Brightness Value (Beta)", "Contrast and Brightness (Linear)", alpha,200, alpha_track_bar)
cv.createTrackbar("Contrast Value (Alpha)", "Contrast and Brightness (Linear)", beta, 200,beta_track_bar)
cv.createTrackbar("Gamma Value", "Gamma (Nonlinear)", gamma, 200, gamma_track_bar)
#initialize
alpha_track_bar(100)
beta_track_bar(100)

cv.waitKey()

cv.imwrite("Linear_Adjusted_Output.jpg", image_bc)
cv.imwrite("Gamma_Correction_Contrast_Output.jpg", image_g)

cv.destroyAllWindows()
