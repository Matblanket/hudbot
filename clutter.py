import numpy as np
import cv2
import touch
import time
typed = {
        "dFTree":10.5,
        "dHTree":10.5,
        "lBTree":15.5,
        "lBush":10.5,
        "lMTree":10.5,
        "lSTree":15.5,
        "pHTree":10.5
        }
def dFTree(currScr):
    clut=cv2.imread('dFTree.png',cv2.IMREAD_UNCHANGED) 
    res=cv2.matchTemplate(currScr,clut,cv2.TM_CCOEFF_NORMED,mask=clut)
    thresh=0.5
    yloc,xloc = np.where(res>=thresh)
    if len(xloc)!=0:
        xloc,yloc=grouP(xloc,yloc)
        for (x,y) in zip(xloc,yloc):
            clear(typed["dFTree"],x,y)

def dHTree(currScr):
    clut=cv2.imread('dHTree.png',cv2.IMREAD_UNCHANGED) 
    res=cv2.matchTemplate(currScr,clut,cv2.TM_CCOEFF_NORMED,mask=clut)
    thresh=0.5
    yloc,xloc = np.where(res>=thresh)
    if len(xloc)!=0:
        xloc,yloc=grouP(xloc,yloc)
        for (x,y) in zip(xloc,yloc):
            clear(typed["dHTree"],x,y)

def lBTree(currScr):
    clut=cv2.imread('lBTree.png',cv2.IMREAD_UNCHANGED) 
    res=cv2.matchTemplate(currScr,clut,cv2.TM_CCOEFF_NORMED,mask=clut)
    thresh=0.5
    yloc,xloc = np.where(res>=thresh)
    if len(xloc)!=0:
        xloc,yloc=grouP(xloc,yloc)
        for (x,y) in zip(xloc,yloc):
            clear(typed["lBTree"],x,y)

def lBush(currScr):
    clut=cv2.imread('lBush.png',cv2.IMREAD_UNCHANGED) 
    res=cv2.matchTemplate(currScr,clut,cv2.TM_CCOEFF_NORMED,mask=clut)
    thresh=0.5
    yloc,xloc = np.where(res>=thresh) 
    if len(xloc)!=0:
        xloc,yloc=grouP(xloc,yloc)
        for (x,y) in zip(xloc,yloc):
            clear(typed["lBush"],x,y)

def lMTree(currScr):
    clut=cv2.imread('lMTree.png',cv2.IMREAD_UNCHANGED) 
    res=cv2.matchTemplate(currScr,clut,cv2.TM_CCOEFF_NORMED,mask=clut)
    thresh=0.5
    yloc,xloc = np.where(res>=thresh)
    if len(xloc)!=0:
        xloc,yloc=grouP(xloc,yloc)
        for (x,y) in zip(xloc,yloc):
            clear(typed["lMTree"],x,y)

def lSTree(currScr):
    clut=cv2.imread('lSTree.png',cv2.IMREAD_UNCHANGED) 
    res=cv2.matchTemplate(currScr,clut,cv2.TM_CCOEFF_NORMED,mask=clut)
    thresh=0.5
    yloc,xloc = np.where(res>=thresh)
    if len(xloc)!=0:
        xloc,yloc=grouP(xloc,yloc)
        for (x,y) in zip(xloc,yloc):
            clear(typed["lSTree"],x,y)

def pHTree(currScr):
    clut=cv2.imread('pHTree.png',cv2.IMREAD_UNCHANGED) 
    res=cv2.matchTemplate(currScr,clut,cv2.TM_CCOEFF_NORMED,mask=clut)
    thresh=0.5
    yloc,xloc = np.where(res>=thresh)
    if len(xloc)!=0:
        xloc,yloc=grouP(xloc,yloc)
        for (x,y) in zip(xloc,yloc):
            clear(typed["pHTree"],x,y)

def grouP(xloc,yloc):
    m=np.array([])
    n=np.array([])
    print("here")
    m=np.append(m,xloc[0])                                                
    n=np.append(n,yloc[0])
    for a in range(1,len(xloc)):
        fl=1
        for l in range(len(m)):
            print("1")
            if m[l]-10<xloc[a]<m[l]+10:
                fl=0
                break
        print(m)
        if fl==1:
            m=np.append(m,xloc[a])
            n=np.append(n,yloc[a])

    return m,n

def clear(pause,x,y):
    touch.tap_screen(x+20,y+20)
    time.sleep(0.5)
    touch.tap_screen(1200,900)
    time.sleep(pause)
