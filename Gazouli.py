import math
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Python gradient calculation

# Read image
im = cv2.imread('test.jpg')
image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Image To Matrix
tab = np.array(image)
print(tab.shape)
'''tab = np.array([[ 63, 173, 131, 205, 239, 108, 241, 155, 63, 173, 131, 205, 239, 108, 241, 155],
                [106,  37, 156,  48,  81, 202,   2, 236, 63, 173, 131, 205, 239, 108, 241, 155],
                [ 85,  85, 119,  60, 228, 214, 141,   1, 63, 173, 131, 205, 239, 108, 241, 155],
                [236,  79, 247,   1, 206,   4, 234, 249, 63, 173, 131, 205, 239, 108, 241, 155],
                [ 97,  50, 117,  96, 206, 232, 217, 116, 63, 173, 131, 205, 239, 108, 241, 155],
                [179, 155,  41,  47, 190,  68,   6,  69, 63, 173, 131, 205, 239, 108, 241, 155],
                [159,  69, 211,  41,  92, 213, 133, 139, 63, 173, 131, 205, 239, 108, 241, 155],
                [ 64, 184, 187, 104, 245, 236,  69, 148, 63, 173, 131, 205, 239, 108, 241, 155],
                [ 63, 173, 131, 205, 239, 108, 241, 155, 63, 173, 131, 205, 239, 108, 241, 155],
                [106,  37, 156,  48,  81, 202,   2, 236, 63, 173, 131, 205, 239, 108, 241, 155],
                [ 85,  85, 119,  60, 228, 214, 141,   1, 63, 173, 131, 205, 239, 108, 241, 155],
                [236,  79, 247,   1, 206,   4, 234, 249, 63, 173, 131, 205, 239, 108, 241, 155],
                [ 97,  50, 117,  96, 206, 232, 217, 116, 63, 173, 131, 205, 239, 108, 241, 155],
                [179, 155,  41,  47, 190,  68,   6,  69, 63, 173, 131, 205, 239, 108, 241, 155],
                [159,  69, 211,  41,  92, 213, 133, 139, 63, 173, 131, 205, 239, 108, 241, 155],
                [ 64, 184, 187, 104, 245, 236,  69, 148, 63, 173, 131, 205, 239, 108, 241, 155]

                ]) '''



cellSize_r = 4
cellSize_c = 4
def Calculate_Hist(img):
    Histogram = []  # definir un tableau pour pour calculer l'histogram de l'image
    for i in range(0, 256):  # remplir la table avec des 0
        Histogram.append(0)
    for i in range(img.shape[0]):  # La boucle pour calculer l'histogram de l'image4
        for j in range(img.shape[1]):
            Histogram[img[i, j]] += 1
    return Histogram

BlockHist = []
AllBlocks = []

Height = int((tab.shape[0]/cellSize_r) - 1)
Width  = int((tab.shape[1]/cellSize_r) - 1)

print('H= ',Height)
print('W = ',Width)
k = 0
i = 0

for r in range(0, tab.shape[0], cellSize_r):
    j = 0
    if i < Height:
        for x in range(7):
            histTemp = []
            AllBlocks.append(histTemp)

    #print(len(AllBlocks))
    print("i=", i)
    for c in range(0, tab.shape[1], cellSize_c):
        #print ("Ligne =",r)
        #print ("Colonne =", c)
        #tab1 = tab[r:r + cellSize_r, c:c + cellSize_c]
        #Calculate_Hist(tab1)

        #print("k using =", k)
        if i == 0 :
            if (j==0):
                AllBlocks[k].append(str(r) + " " + str(c))
            elif j == Width:
                k1 = k - 1
                AllBlocks[k1].append(str(r) + " " + str(c))
            else :
                AllBlocks[k].append(str(r) + " " + str(c))
                AllBlocks[k-1].append(str(r) + " " + str(c))


        if i > 0 and i < Height:
            if j == 0:
                AllBlocks[k].append(str(r) + " " + str(c))
                AllBlocks[k - Width].append(str(r) + " " + str(c))
            elif j == Width:
                k1 = k - 1
                AllBlocks[k1].append(str(r) + " " + str(c))
                AllBlocks[k1 - j].append(str(r) + " " + str(c))
            else:
                AllBlocks[k].append(str(r) + " " + str(c))
                AllBlocks[k - 1].append(str(r) + " " + str(c))
                AllBlocks[j].append(str(r) + " " + str(c))
                AllBlocks[j-1].append(str(r) + " " + str(c))

        if i == Height:
            if (j==0):
                k = k - (Width)
                AllBlocks[k].append(str(r) + " " + str(c))
            elif j == Width:
                AllBlocks[k-1].append(str(r) + " " + str(c))
            else :
                AllBlocks[k].append(str(r) + " " + str(c))
                AllBlocks[k-1].append(str(r) + " " + str(c))

        if k < len(AllBlocks):
            k += 1

        print("i=", i)
        #print("k afeter + =", k)
        print("j=", j)
        print("k=", k)
        j += 1
        print(AllBlocks)


    i += 1




print("k = ", k)
for  i in range(105):
    print((AllBlocks[i]))





#End of the file