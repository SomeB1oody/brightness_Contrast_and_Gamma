#Author: Stan Yin
#GitHub Name: SomeB1oody
#This project is based on CC 4.0 BY, please mention my name if you use it.
#This project requires opencv.
import cv2 as cv
import numpy as np

print("Please enter the path of the image\t")
print("Example: C:\\Wallpaper\\02.jpg\t")
location = input("Enter HERE: ")
original_img = cv.imread(location, cv.IMREAD_COLOR)
if original_img is None:
    raise ValueError("Couldn't load the image")
global image_bc, image_bco, image_g, image_go
alpha = 100
beta = 100
gamma = 100

def contrast_brightness_adjustment(input_image, _alpha, _beta):
    global image_bc, image_bco
    output_image = cv.convertScaleAbs(input_image, alpha=_alpha, beta=_beta)
    image_bc = cv.hconcat(input_image, output_image)
    cv.imshow("Contrast Brightness", image_bc)
    image_bco = output_image

def gamma_correction(input_image, _gamma):
    global image_g, image_go
    assert _gamma >= 0, "Gamma value should be non-negative."
    look_up_table = np.zeros((256,), dtype=np.uint8)
    for index in range(256):
        value = np.clip((index / 255.0) ** _gamma * 255.0, 0, 255)
        look_up_table[index] = np.uint8(value)
    image_go = cv.LUT(input_image, look_up_table)
    image_g = cv.hconcat(input_image, image_go)
    cv.imshow("Gamma (Nonlinear)", image_g)

def alpha_track_bar(_alpha):
    actual_alpha_value = _alpha / 100.0
    actual_beta_value = beta - 100
    contrast_brightness_adjustment(original_img, actual_alpha_value, actual_beta_value)

def beta_track_bar(_beta):
    actual_alpha_value = alpha / 100.0
    actual_beta_value = _beta - 100
    contrast_brightness_adjustment(original_img, actual_alpha_value, actual_beta_value)

def gamma_track_bar(_gamma):
    actual_gamma_value = _gamma / 100.0
    gamma_correction(original_img, actual_gamma_value)

cv.namedWindow("Contrast and Brightness (Linear)", cv.WINDOW_AUTOSIZE)
cv.namedWindow("Gamma (Nonlinear)", cv.WINDOW_AUTOSIZE)
cv.createTrackbar("Contrast Value (Alpha)", "Contrast and Brightness (Linear)", alpha,200, alpha_track_bar)
cv.createTrackbar("Brightness Value (Beta)", "Contrast and Brightness (Linear)", beta, 200,beta_track_bar)
cv.createTrackbar("Gamma Value", "Gamma (Nonlinear)", gamma, 200, gamma_track_bar)

alpha_track_bar(100)
beta_track_bar(100)

cv.waitKey()

cv.imwrite("Linear_Adjustment_Contrast_Output.jpg", image_bc)
cv.imwrite("Linear_Adjusted_Output.jpg", image_bco)
cv.imwrite("Gamma_Correction_Contrast_Output.jpg", image_g)
cv.imwrite("Gamma_Corrected_Output.jpg", image_go)

cv.destroyAllWindows()
