import numpy as np
import cv2
import touch
def colRes(currScr,colImg):
    temp=cv2.matchTemplate(currScr,colImg,cv2.TM_CCOEFF_NORMED)
    lval,mval,lloc,mloc=cv2.minMaxLoc(temp)
    touch.tap_screen(mloc[0],mloc[1])
