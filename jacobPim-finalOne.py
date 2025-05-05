import numpy as np
import cv2

square =np.zeros((8, 8), dtype=np.uint8)

def makeCol(end1, end2):
    array = []
    for i in range(8):
        value = int((end2 * i/7) + (end1 * (7-i)/7))
        array.append(value)

    return array

def makeRow(end1, end2, row):
    for i in range(8):
        value = int((end2 * i/7) + (end1 * (7 - i)/7))
        square[row][i] = value

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