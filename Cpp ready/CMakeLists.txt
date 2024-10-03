cmake_minimum_required(VERSION 3.29)
project(brightness_Contrast_and_Gamma)

set(CMAKE_CXX_STANDARD 14)

add_executable(
    "BCG ConvertTo.cpp"
    "BCG no ConvertTo.cpp")

set(OpenCV_DIR "C:/opencv/build/x64/vc16/lib/")
find_package(OpenCV REQUIRED)
include_directories(brightness_Contrast_and_Gamma ${OpenCV_INCLUDE_DIRS})
target_link_libraries(brightness_Contrast_and_Gamma ${OpenCV_LIBS})
