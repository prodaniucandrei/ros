#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import cv2
import os
import numpy as np
import sys, select, termios, tty
import time
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import glob

lowerBound=np.array([170,70,50])    # 0 70 50     
#lower 109 12 21
upperBound=np.array([179,255,255])   #10 255 255
#upper 193 103 97

#lowerBound=np.array([177,226,42])
#upperBound=np.array([2,127,75])

kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

if __name__=="__main__":

    '''
    script_dir = os.path.dirname(__file__)
    rel_path = "image.png"
    abs_file_path = os.path.join(script_dir, rel_path)
    
    file = open(abs_file_path,'r')
    image_data = np.asarray(file)
    image_data=cv2.resize(image_data,(340,220))
    '''
   
    image_data = cv2.imread('/home/aprodaniuc/Pictures/clivsc.png',1)
    cv2.imshow('img2',image_data)
    image_data=cv2.resize(image_data,(340,220))
    

    imgHSV= cv2.cvtColor(image_data,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)

    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    hist = cv2.calcHist([image_data],[0],None,[256],[0,256])

    plt.plot(hist)
    plt.show()

    cv2.imshow("maskClose",maskClose)
    cv2.imshow("maskOpen",maskOpen)
    cv2.imshow("mask",mask)
    cv2.imshow("hist",hist)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()