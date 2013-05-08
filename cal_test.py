#!/usr/bin/env python

import cv, pickle
dims=(17,17)
c=cv.CaptureFromCAM(1)
while True:
    f=cv.QueryFrame(c)
    grey=cv.CreateImage((640,480),8,1)
    cv.CvtColor(f,grey,cv.CV_BGR2GRAY)
    found,points=cv.FindChessboardCorners(grey,dims)
    if found!=0:
        cv.DrawChessboardCorners(f,dims,points,found)
        cv.SaveImage("corners.png",f)
        with open('points.dat','wb') as p:
            pickle.dump(points,p)
        break
