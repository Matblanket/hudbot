import clutter
import cv2
import test
currScr=cv2.imread('sc.png',-1)
clutter.lBTree(currScr)
clutter.dFTree(currScr)
clutter.dHTree(currScr)
clutter.lBush(currScr)
clutter.lMTree(currScr)
clutter.lSTree(currScr)
clutter.pHTree(currScr)
