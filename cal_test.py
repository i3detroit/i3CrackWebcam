#!/usr/bin/env python

import cv
dims=(40,40)
c=cv.CaptureFromCAM(1)
while True:
    f=cv.QueryFrame(c)
    grey=cv.CreateImage((640,480),8,1)
    cv.CvtColor(f,grey,cv.CV_BGR2GRAY)
    found,points=cv.FindCirclesGrid(grey,dims)
    if found!=0:
        cv.DrawChessboardCorners(f,dims,points,found)
        cv.ShowImage("win2",f)
        cv.WaitKey(2)
