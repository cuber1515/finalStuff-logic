import numpy as np
import cv2

from scipy.special import comb

square =np.zeros((8, 8), dtype=np.uint8)

def smoothstep(x, x_min=0, x_max=1, N=1):
    x = np.clip((x - x_min) / (x_max - x_min), 0, 1)

    result = 0
    for n in range(0, N + 1):
         result += comb(N + n, n) * comb(2 * N + 1, N - n) * (-x) ** n

    result *= x ** (N + 1)

    return result

def makeCol(end1, end2):
    array = []
    s = smoothstep(0, 0, 1, 1)
    for i in range(8):
        value = int((end2 * s) + (end1 * (1 - s)))
        array.append(value)
        s = smoothstep(i, 0, 7, 1)

    return array

def makeRow(end1, end2, row):
    s = smoothstep(0, 0, 1, 1)
    for i in range(8):
        value = int((end2 * s) + (end1 * (1 - s)))
        square[row][i] = value
        s = smoothstep(i, 0, 7, 1)

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