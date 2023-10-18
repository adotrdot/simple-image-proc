"""
Tugas 3 Pengolahan Citra Digital
Percobaan Efek Twirl pada Gambar
"""

# Library
import math
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Fungsi efek spherical
def twirl(original_img, a):
    height, width = original_img.shape

    new_img = original_img.copy()
    xc = round((width-1)/2)
    yc = round((height-1)/2)
    alpha = a * math.pi / 180
    rmaks = 0.5 * math.sqrt(xc ** 2 + yc ** 2) # 1/2 diagonal citra
    for y in range(1, height-1):
        for x in range(1, width-1):
            r = math.sqrt((x-xc) ** 2 + (y-yc) ** 2)
            beta = math.atan2(y-yc, x-xc) + \
                    alpha * (rmaks - r) / rmaks
            new_x = xc + r * math.cos(beta)
            new_y = yc + r * math.sin(beta)

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

# Implementasi efek twirl
new_img = twirl(img, 43)

cv.imshow("Hasil", new_img)
cv.waitKey(0)
cv.destroyAllWindows()