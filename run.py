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

video = cv2.VideoCapture('assets/[HD] Touhou - Bad Apple!! [ＰＶ] (Shadow Art)-UkgK8eUdpAo.f247.webm')
frameCount = 0
frameRate = 15

input("Press Enter to continue...")
while True:
    startTime = time.time()
    success,frame = video.read()
    if not success:
        break;
    scaledFrame = cv2.resize(frame,dsize=(0,0),fx=0.15,fy=0.07,interpolation=cv2.INTER_CUBIC)
    grayFrame = cv2.cvtColor(scaledFrame,cv2.COLOR_RGB2GRAY)
    invertedFrame = cv2.bitwise_not(grayFrame)
    finalFrame = invertedFrame / 255.0;

    #print(finalFrame.shape);
    #np.savetxt('lel.txt',finalFrame,delimiter=' ',newline='\n')
    
    #print(endTime - startTime)
    #break
    printFrame(finalFrame.astype(int))
    endTime = time.time();
    time.sleep((1/frameRate));
    takeScreenshot("out/image-%d.png" % frameCount)
    clear()
    frameCount += 1
    #break
    
    