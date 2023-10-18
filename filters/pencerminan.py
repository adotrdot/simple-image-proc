"""
Tugas 3 Pengolahan Citra Digital
Percobaan Pencerminan Gambar
"""

# Library
import math
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Function pencerminan gambar
def pencerminan_vertical(original_img):
    return cv.flip(original_img, 0)

def pencerminan_horizontal(original_img):
    return cv.flip(original_img, 1)

def pencerminan_all(original_img):
    return cv.flip(original_img, -1)


# Membaca gambar
img = cv.imread('mobil.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "File tidak dapat dibaca"

# new_img = pencerminan_vertical(img)
# new_img = pencerminan_horizontal(img)
new_img = pencerminan_all(img)

cv.imshow("Hasil", new_img)
cv.waitKey(0)
cv.destroyAllWindows()