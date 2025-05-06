import numpy as np
import cv2
from scipy.special import comb
from random import randint

square =np.zeros((15, 15), dtype=np.uint8)

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

def makeRow(end1, end2, row, right):
    s = smoothstep(0, 0, 1, 1)
    for i in range(8):
        value = int((end2 * s) + (end1 * (1 - s)))
        if right:
            square[row][i + 7] = value
        else:
            square[row][i] = value

        s = smoothstep(i, 0, 7, 1)

nein = [randint(0, 255) for i in range(9)]

tlLeft = makeCol(nein[0], nein[1])
tlRight = makeCol(nein[2], nein[3])

blLeft = makeCol(nein[1], nein[4])
blRight = makeCol(nein[3], nein[5])

trLeft = tlRight
trRight = makeCol(nein[6], nein[7])

brLeft = blRight
brRight = makeCol(nein[7], nein[8])

for i in range(8):
    makeRow(tlLeft[i], tlRight[i], i, False)
    makeRow(blLeft[i], blRight[i], i + 7, False)
    makeRow(trLeft[i], trRight[i], i, True)
    makeRow(brLeft[i], brRight[i], i + 7, True)

cv2.namedWindow("Gradient",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gradient",600,600)
cv2.imshow("Gradient",square)
cv2.waitKey()