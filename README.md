# License-Plate-Detection-Using-OpenCV
Detect vehicle license plates using basic computer vision techniques

Using several built-in threshold methods and a contour estimation method from OpenCV library to detect license plates from images of vehicles.
The detected license plate bounding box can be cropped and passed to an OCR to read the license number. Here, we use the Pytesseract OCR library for python.

## Sample Outputs
1.
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/imgs/car_2.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/imgs/ths1.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/imgs/th1.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/imgs/op1.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/imgs/n1.jpg)

2.
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/imgs/car_3.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/imgs/ths2.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/imgs/th2.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/imgs/op2.jpg)
![alt text](https://raw.githubusercontent.com/antrix99/License-Plate-Detection-Using-OpenCV/master/imgs/n2.jpg)

## Limitations

Since the thresholding parameters are hard-coded, results are specific to the image brightness and other lighting conditions.
