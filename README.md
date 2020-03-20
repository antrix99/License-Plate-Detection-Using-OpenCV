# License-Plate-Detection-Using-OpenCV
Detect vehicle license plates using basic computer vision techniques

Using several built-in threshold methods and a contour estimation method from OpenCV library to detect license plates from images of vehicles.
The detected license plate bounding box can be cropped and passed to an OCR to read the license number. Here, we use the Pytesseract OCR library for python.

## Sample Outputs
1.
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/car_2.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/ths1.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/th1.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/op1.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/n1.jpg)

2.
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/car_3.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/ths2.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/th2.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/op2.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/n2.jpg)

## Limitations

Since the thresholding parameters are hard-coded, results are specific to the image brightness and other lighting conditions.
