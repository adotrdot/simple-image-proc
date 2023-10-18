"""
Tugas 3 Pengolahan Citra Digital
Percobaan Rotasi Gambar dengan
a. Titik rotasi (0,0)
b. Titik rotasi sembarang
c. Titik rotasi pusat citra
"""

# Library
import math
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Function rotasi gambar
def rotasi_titik_nol(original_img, angle):
    height, width = original_img.shape

    matriks = cv.getRotationMatrix2D((0,0), angle, 1)
    new_img = cv.warpAffine(original_img, matriks, (width, height))
    return new_img

def rotasi_titik_sembarang(original_img, sumbu_x, sumbu_y, angle):
    height, width = original_img.shape

    matriks = cv.getRotationMatrix2D((sumbu_x, sumbu_y), angle, 1)
    new_img = cv.warpAffine(original_img, matriks, (width, height))
    return new_img

def rotasi_titik_pusat(original_img, angle):
    height, width = original_img.shape

    matriks = cv.getRotationMatrix2D((height/2, width/2), angle, 1)
    new_img = cv.warpAffine(original_img, matriks, (width, height))
    return new_img


# Membaca gambar
img = cv.imread('mobil.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "File tidak dapat dibaca"

new_img = rotasi_titik_nol(img, -10)
# new_img = rotasi_titik_sembarang(img, 30, 40, -10)
# new_img = rotasi_titik_pusat(img, -20)

cv.imshow("Hasil", new_img)
cv.waitKey(0)
cv.destroyAllWindows()