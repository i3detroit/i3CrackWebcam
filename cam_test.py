#!/usr/bin/env python
import cv
import os

print os.getcwd()

capture=cv.CaptureFromCAM(1)
count=0
threshold = 192
colour = 255
while count<250:
    image=cv.QueryFrame(capture)
    grey=cv.CreateImage((640,480),8,1)
    cv.CvtColor(image,grey,cv.CV_BGR2GRAY)
    cv.EqualizeHist(grey,grey)
    cv.Threshold(grey,grey, threshold,colour,cv.CV_THRESH_OTSU)
    cv.ShowImage('Image_Window',grey)

#    grey=cv.CreateImage((640,480),8,1)
#    cv.CvtColor(image,grey,cv.CV_BGR2GRAY)
    dst_16s2 = cv.CreateImage(cv.GetSize(grey), cv.IPL_DEPTH_16S, 1)
    cv.Laplace(grey, dst_16s2,3)
    cv.Convert(dst_16s2,image)
    cv.ShowImage('Laplace_Window',image)

    print count
    cv.WaitKey(2)
    count+=1
