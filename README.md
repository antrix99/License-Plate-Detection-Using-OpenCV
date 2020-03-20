# License-Plate-Detection-Using-OpenCV
Detect vehicle license plates using basic computer vision techniques

Using several built-in threshold methods and a contour estimation method from OpenCV library to detect license plates from images of vehicles.

The detected license plate bounding box can be cropped and passed to an OCR to read the license number. Here, we use the Pytesseract OCR library for python.

## Limitations

Since the thresholding parameters are hard-coded, results are specific to the image brightness and other lighting conditions.
