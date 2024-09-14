/*Author: Stan Yin
* GitHub Name: SomeB1oody
* This project is based on CC 4.0 BY, please mention my name if you use it.
* This project requires opencv.
*/
#include<bits/stdc++.h>
#include<opencv2/opencv.hpp>
using namespace std;
using namespace cv;

namespace
{
	int _alpha = 100, _beta = 100, _gamma = 100;
	Mat image, imageCB, imageG, imageCBO, imageGO;
	void  CBAdjust(Mat inputImage, double alpha, int beta)
	{
		cout << endl << endl << endl << endl << endl;
		cout << "Contrast and brightness are adjusting"<<endl;
		Mat outputImage;
		inputImage.convertTo(outputImage, -1, _alpha, _beta);
		cout << "----------------------Adjust Successfully--------------------";
		hconcat(inputImage, outputImage, imageCB);
		imshow("Brightness and Contrast (Linear)", imageCB);
		imageCBO = outputImage;
	}
	void gammaCorrect(Mat inputImage, double gammavalue)
	{
		cout << endl << endl << endl << endl << endl;
		cout << "Gamma is correcting" << endl;
		cout << "schedule:" << endl;
		CV_Assert(gammavalue >= 0);
		Mat lookUpTable(1, 256, CV_8U);
		uchar* pointer = lookUpTable.ptr();
		cout << "filling lookUpTable: ";
		for (int index = 0; index < 256; ++index)
		{
			pointer[index] = saturate_cast<uchar>(pow(index / 255.0, gammavalue) * 255.0);
			cout << index + 1 << "/256"<<endl;
		}
		cout << "cloning"<<endl;
		Mat process = image.clone();
		cout << "transforming" << endl;
		LUT(image, lookUpTable, process);
		cout << "----------------------Correct Successfully--------------------";
		hconcat(inputImage, process, imageG);
		imshow("Gamma (Nolinear)", imageG);
		imageGO = process;
	}
	void alphaTrack(int, void*)
	{
		cout << endl << "invoking adjustment function" << endl;
		double actualAlphaValue = _alpha / 100.0;
		int actualBetaValue = _beta - 100;
		CBAdjust(image, actualAlphaValue, actualBetaValue);
	}
	void betaTrack(int, void*)
	{
		cout << endl << "invoking adjustment function" << endl;
		double actualAlphaValue = _alpha / 100.0;
		int actualBetaValue = _beta - 100;
		CBAdjust(image, actualAlphaValue, actualBetaValue);
	}
	void gammaTrack(int, void*)
	{
		cout << endl << "invoking correction function" << endl;
		double gamma_value = _gamma / 100.0;
		gammaCorrect(image, gamma_value);
	}
}
int main(int argc, char** argv)
{
	string location;
	cout << "Please enter image's location" << endl;
	cout << "Example: C:\\Wallpaper\\Picture.jpg" << endl;
	cin >> location;
	Mat image = imread(location, IMREAD_COLOR);
	if (image.empty())
	{
		cout << "Cannot load image" << endl;
		return -1;
	}
	imageCB = Mat(image.rows, image.cols * 2, image.type());
	imageG = Mat(image.rows, image.cols * 2, image.type());
	hconcat(image, image, imageCB);
	hconcat(image, image, imageG);
	cout << "-------------------------build Success----------------------" << endl;
	namedWindow("Brightness and Contrast (Linear)");
	namedWindow("Gamma (Nolinear)");
	createTrackbar("Contrast (Alpha)", "Brightness and Contrast (Linear)", &_alpha, 500, alphaTrack);
	createTrackbar("Brightness (Beta)", "Brightness and Contrast (Linear)", &_beta, 200, betaTrack);
	createTrackbar("Gamma", "Gamma (Nolinear)", &_gamma, 200, gammaTrack);
	alphaTrack(0, 0);
	gammaTrack(0, 0);
	waitKey();
	imwrite("Linear_Adjustment_Contrast_Output.jpg", imageCB);
	imwrite("Gamma_Correction_Contrast_Output.jpg", imageG);
	imwrite("Linear_Adjusted_Output.jpg", imageCBO);
	imwrite("Gamma_Corrected_Output.jpg", imageGO);
	return 0;
}
