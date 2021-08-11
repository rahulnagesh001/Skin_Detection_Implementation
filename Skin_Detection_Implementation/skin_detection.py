# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:49:00 2021

@author: Rahul
"""

import PIL
import numpy as np
from datetime import datetime

#function to  check if r,g,b,a values values lie in a range of predefined threshold values for a skin pixel
def rgba_check(pr,pg,pb,a):
    if pr > 95 and pg >40 and pb >40 and pr > pg and pr > pb:
        if abs(pr - pb) > 15 and a >15:
            return True
    return False




#function to  check Y,Cb,Cr values values lie in a range of predefined threshold values for a skin pixel
def ycbcr_check(py,pcb,pcr):
    if py >80 and pcb >85 and pcr >135:
         if pcr <= (1.5862 * pcb) + 20 and pcr >= (0.3448 * pcb) + 76.2069:
            if pcr >= (-4.5652 * pcb) + 234.5652 and pcr <= (-1.15 * pcb) + 301.75 and pcr <= (-2.2857 * pcb) + 432.85:
             return True
    return False  


#function to detect skin pixels in the image
def detect_skin_pixels(image):
    # convert image to RGBA
    image = image.convert('RGBA')
    
    #get dimensions of the image
    width, height = image.size
    
    
    #converting image to nparray 
    data = np.asarray(image)
    
    
    # convert image to YCbCr
    ycbcr = image.convert('YCbCr')
    data_ycbcr = np.asarray(ycbcr)
    
    #copying the original image to output - for processing
    output = image
    
    #iterate over each pixel in the image checking if it is a skin pixel
    for r,row in enumerate(data):
        for c,pixel in enumerate(row):
             y = data_ycbcr[r][c][0]
             cb =data_ycbcr[r][c][1]
             cr = data_ycbcr[r][c][2]
             red = pixel[0]
             green = pixel[1]
             blue = pixel[2]
             alpha = pixel[3]
             if rgba_check(red,green,blue,alpha) and ycbcr_check(y,cb,cr): 
                 output.putpixel((c,r),(255,255,255))
                 continue         
             output.putpixel((c,r),(0,0,0))      
    display(output)
    

#function to display image
def display(image):
    image.show()
    

#Load the image, display it and pass it for processing
def detect_skin():
  
    #Load image to memory - RGB by default
    image = PIL.Image.open("0016.jpg")
    #image = PIL.Image.open("D:/Echobatix/Skin_Detection_Implementation/IMG_20210108_170752 (2).jpg")
        
    #show Original Image
    display(image)
    
    
    ta = datetime.now()
    #detect the skin pixels and display resulting image with only skin pixels
    detect_skin_pixels(image)
    
    tb = datetime.now()
    
    td = tb - ta
    print("processing time:",td)
    



#Run skin detection program
detect_skin()