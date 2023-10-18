"""
Tugas 3 Pengolahan Citra Digital
Percobaan Transformasi Bilinear pada Gambar
"""

# Library
import math
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Fungsi transformasi bilinear
def tbilin(original_img, a1, a2, a3, a4, b1, b2, b3, b4):
    height, width = original_img.shape

    new_img = original_img.copy()
    for y in range(1, height-1):
        for x in range(1, width-1):
            new_x = a1*x + a2*y + a3*x*y + a4
            new_y = b1*x + b2*y + b3*x*y + b4

            if new_x >= 1 and new_x <= width-1 and new_y >= 1 and new_y <= height-1:
                # Lakukan interpolasi bilinear
                p = math.floor(new_y)
                q = math.floor(new_x)
                a = new_y - p
                b = new_x - q

                if math.floor(new_x) == width-1 or math.floor(new_y) == height-1:
                    new_img.itemset((y,x), original_img.item(math.floor(new_y), math.floor(new_x)))
                else:
                    intensitas = (1-a)*((1-b)*original_img.item(p,q)+b*original_img.item(p,q+1)) + \
                                    a*((1-b)*original_img.item(p+1,q)+b*original_img.item(p+1,q+1))
                    new_img.itemset((y,x), intensitas)
            else:
                new_img.itemset((y,x), 0)

    return new_img

# Membaca gambar
img = cv.imread('mobil.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "File tidak dapat dibaca"

# Implementasi transformasi bilinear
new_img = tbilin(img,1.2,0.1,0.005,-45,0.1,1,0.005,-30)

cv.imshow("Hasil", new_img)
cv.waitKey(0)
cv.destroyAllWindows()