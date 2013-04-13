#!/usr/bin/env python

import cv
capture=cv.CaptureFromCAM(1)
cv.WaitKey(200)
frame=cv.QueryFrame(capture)
temp=cv.CloneImage(frame)
cv.Smooth(temp,temp,cv.CV_BLUR,5,5)
while True:
    frame=cv.QueryFrame(capture)
    cv.AbsDiff(frame,temp,frame)
    cv.ShowImage("Windo2w",temp)
    cv.ShowImage("Window",frame)
    c=cv.WaitKey(2)
    if c==27: #Break if user enters 'Esc'.
        break
