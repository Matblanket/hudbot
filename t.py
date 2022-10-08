import colect
import touch
import cv2
import numpy as np
import time
elixCoImg=cv2.imread('elixco.png',-1)
goldCoImg=cv2.imread('goldco.png',-1)
delixCoImg=cv2.imread('delixco.png',-1)
colect.colRes(cv2.imread('sc.png',-1),elixCoImg)
colect.colRes(cv2.imread('sc.png',-1),goldCoImg)
colect.colRes(cv2.imread('sc.png',-1),delixCoImg)
