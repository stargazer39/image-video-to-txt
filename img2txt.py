import cv2
import numpy as np
import time
import os
import pyautogui

clear = lambda: os.system('cls')
def printFrame (frame):
    out = ""
    for i in frame:
        for j in i:
            if j == 0:
                out += ' '
                #print(' ',end='')
            else:
                out += '@'
                #print('@',end='')
        out += "\n"
    print(out,flush=True)
            
def takeScreenshot(filename):
    # take screenshot using pyautogui
    image = pyautogui.screenshot()
    
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    
    # writing it to the disk using opencv
    cv2.imwrite(filename, image)

img = cv2.imread('assets\outro.png')

input("Press Enter to continue...")
scaledFrame = cv2.resize(img,dsize=(0,0),fx=0.033,fy=0.017,interpolation=cv2.INTER_CUBIC)
grayFrame = cv2.cvtColor(scaledFrame,cv2.COLOR_RGB2GRAY)
invertedFrame = cv2.bitwise_not(grayFrame)
finalFrame = invertedFrame / 255.0;

printFrame(finalFrame)

    
    