cmake_minimum_required(VERSION 3.29)
project(CPP)

set(CMAKE_CXX_STANDARD 14)

add_executable(BCG.cpp
    "Affine transformation.cpp"
    "BCG  ConvertTo.cpp"
    "QR Code Decoder.cpp"
    small_img_cpp_version.cpp)

set(OpenCV_DIR "C:/opencv/build/x64/vc16/lib/")
find_package(OpenCV REQUIRED)
include_directories(BCG.cpp small_img_cpp_version.cpp ${OpenCV_INCLUDE_DIRS})
target_link_libraries(BCG.cpp small_img_cpp_version.cpp ${OpenCV_LIBS})