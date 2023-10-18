"""
Tugas 3 Pengolahan Citra Digital
Percobaan Scaling Gambar
"""

# Library
import math
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Function scale gambar
def scale(original_img, scale_x, scale_y):
    return cv.resize(original_img, None, fx=scale_x, fy=scale_y)


# Membaca gambar
img = cv.imread('mobil.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "File tidak dapat dibaca"

new_img = scale(img, 4, 2)

cv.imshow("Hasil", new_img)
cv.waitKey(0)
cv.destroyAllWindows()