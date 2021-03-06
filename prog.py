import numpy as np, pandas as pd, cv2, matplotlib.pyplot as plt, pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img=cv2.imread('..\\car_2.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
re, threshold=cv2.threshold(gray,200,
                            255,cv2.THRESH_TOZERO_INV)
ret, thresho=cv2.threshold(threshold,170,
                            255,cv2.THRESH_TOZERO)
ret, thresh=cv2.threshold(thresho,170,
                            255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL, 
                                    cv2.CHAIN_APPROX_SIMPLE)

#Threshold range for 2nd image(serially): (240,255)(230,255)(170,255)

detected=[]
for i in contours:
    rect=cv2.minAreaRect(i)
    box=cv2.boxPoints(rect)
    box=np.int0(box)
    if rect[1][0]>10 and rect[1][1]>=30:
        cv2.drawContours(img,[box],0,(0,255,100),2)
        detected.append([box[2],box[0]])
    else:
        cv2.drawContours(img,[box],0,(0,0,255),1)

cv2.imshow('t1',threshold)
cv2.imshow('t2',thresho)
cv2.imshow('t3',thresh)
cv2.imshow('t',img)


nplt=[]
for i in detected:
    y1,x1,y2,x2=i[0][0],i[0][1],i[1][0],i[1][1]
    if x1>0 and y1>0 and x2>0 and y2>0:
        nplt.append(img[x1:x2,y1:y2])
        
cv2.imshow('n',nplt[0])
reg_num=[]
for i in nplt:
    reg_num.append(pytesseract.image_to_string(i))'

    
    
    
