"""
Tugas 3 Pengolahan Citra Digital
Percobaan Efek Ripple pada Gambar
"""

# Library
import math
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Fungsi efek ripple
def ripple(original_img, ax, ay, tx, ty):
    height, width = original_img.shape

    new_img = original_img.copy()
    for y in range(1, height-1):
        for x in range(1, width-1):
            new_x = x + ax * math.sin(2 * math.pi * y / tx)
            new_y = y + ay * math.sin(2 * math.pi * x / ty)
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

# Implementasi efek ripple
new_img = ripple(img,10,15,120,250)

cv.imshow("Hasil", new_img)
cv.waitKey(0)
cv.destroyAllWindows()