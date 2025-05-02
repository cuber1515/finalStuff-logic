import numpy as np
import cv2

square =np.zeros((8, 8), dtype=np.uint8)

def makeCol(end1, end2):
    min_num = min(end1, end2)
    max_num = max(end1, end2)
    gap = max_num - min_num
    interval = gap / 7
    array = []
    for i in range(8):
        array.append(int(min_num + (interval * i)))

    return array

def makeRow(end1, end2, row):
    min_num = min(end1, end2)
    max_num = max(end1, end2)
    gap = max_num - min_num
    interval = gap / 7
    for i in range(8):
        square[row][i] = int(min_num + (interval * i))

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