import cv2 as cv
import sys
import numpy as np
import time

filenums = ["020",'021','033','034','397','417','446','450']

file1 = f"Sample_Pictures/Flowers/DSC_0020.jpg"
file2 = f"Sample_Pictures/Flowers/DSC_0033.jpg"

alpha = 1.0
beta = 0.0
i = 1

img1 = cv.imread(f"Sample_Pictures/Flowers/DSC_0{filenums[i-1]}.jpg")
img2 = cv.imread(f"Sample_Pictures/Flowers/DSC_0{filenums[i]}.jpg")

if [img1, img2] is None:
    sys.exit("Could not read IMG")
i+=1

while True:

    if [img1, img2] is None:
        sys.exit("Could not read IMG")

    dst = cv.addWeighted(img1,alpha,img2,beta,0)
    cv.imshow('dst',dst)

    alpha = alpha-0.1
    beta = beta+0.1

    if alpha <= 0 and beta >=1:
        alpha = 1.0
        beta = 0.0
        if [img1, img2] is None:
            sys.exit("Could not read IMG")

        k = cv.waitKey(0)
        if k == ord("a"):
            if i==1:
                i=len(filenums[i])-1
            else:
                i=i-1

            img1 = cv.imread(f"Sample_Pictures/Flowers/DSC_0{filenums[i+1]}.jpg")
            img2 = cv.imread(f"Sample_Pictures/Flowers/DSC_0{filenums[i]}.jpg")

            if [img1, img2] is None:
                sys.exit("Could not read IMG")

        elif k== ord("x"):
            break

        else:
            i = i + 1

            if (i >= len(filenums) - 1):
                i = 1

            img1 = cv.imread(f"Sample_Pictures/Flowers/DSC_0{filenums[i-1]}.jpg")
            img2 = cv.imread(f"Sample_Pictures/Flowers/DSC_0{filenums[i]}.jpg")

            if [img1, img2] is None:
                sys.exit("Could not read IMG")

    k = cv.waitKey(50)
    if k == ord("x"):
        break

cv.destroyAllWindows()



