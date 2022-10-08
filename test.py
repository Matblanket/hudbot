import numpy as np
import cv2
testLook=cv2.imread('dHTree.png',cv2.IMREAD_UNCHANGED)
fulImg=cv2.imread('sc.png',cv2.IMREAD_UNCHANGED)
channels = cv2.split(testLook)
zero_channel = np.zeros_like(channels[0])
mask = np.array(channels[3])

mask[channels[3] == 0] = 1
mask[channels[3] == 100] = 0

tran_mask=cv2.merge([mask,mask,mask])

res=cv2.matchTemplate(fulImg,testLook,cv2.TM_CCOEFF_NORMED,mask=tran_mask)
w=testLook.shape[1]
h=testLook.shape[0]
thresh=0.3
yloc,xloc = np.where(res>=thresh)
rectangles=[]
for(x,y) in zip(xloc,yloc):
    rectangles.append([int(x),int(y),int(w),int(h)])
rectangles, weights=cv2.groupRectangles(rectangles,1,0.2)
for(x,y,w,h) in rectangles:
    cv2.rectangle(fulImg,(x,y),(x+w,y+h),255,2)
cv2.imshow('f',fulImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
