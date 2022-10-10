import numpy as np
import cv2
def trect(tester):
    currScr=cv2.imread('sc.png',cv2.IMREAD_UNCHANGED)
    res=cv2.matchTemplate(currScr,tester,cv2.TM_CCOEFF_NORMED,mask=tester)
    w=tester.shape[1]
    h=tester.shape[0]
    thresh=0.5
    yloc,xloc = np.where(res>=thresh)
    rectangles=[]
    for(x,y) in zip(xloc,yloc):
        rectangles.append([int(x),int(y),int(w),int(h)])
    rectangles, weights=cv2.groupRectangles(rectangles,1,0.2)
    for(x,y,w,h) in rectangles:
        cv2.rectangle(currScr,(x,y),(x+w,y+h),255,2)
    cv2.imshow('f',currScr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
