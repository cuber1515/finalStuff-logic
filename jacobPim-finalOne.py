import numpy as np
import cv2

square =np.zeros((8, 8), dtype=np.uint8)

def makeCol(end1, end2):
    
    # gap = abs(end1-end2)
    array = []
    for i in range(8):
        value = int((end1 * i/7) + (end2 * i/7)) 
        print(value)
        array.append(value)

    return array

def makeRow(end1, end2, row):
    gap = abs(end1-end2)
    for i in range(8):
        value = int((end1 * i/7) + (end2 * i/7)) 
        square[row][i] = value
        # square[row][i] = 255

nw = 111
ne = 186
sw = 0
se = 255

left = makeCol(nw, sw)
right = makeCol(ne, se)

for i in range(8):
    makeRow(left[i], right[i], i)


cv2.namedWindow("Gradient",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gradient",600,600)
cv2.imshow("Gradient",square)
cv2.waitKey()