"""
Tugas 3 Pengolahan Citra Digital
Percobaan Menggeser Gambar melaluai Sumbu X dan Y
"""

# Library
import math
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Function translasi gambar
def translasi(original_img, sumbu_x, sumbu_y):
    height = original_img.shape[0]
    width = original_img.shape[1]

    new_img = np.zeros((height, width), dtype=np.uint8)

    left = abs(sumbu_x) if sumbu_x < 0 else 0
    right = width if sumbu_x < 0 else width - sumbu_x

    top = abs(sumbu_y) if sumbu_y < 0 else 0
    bottom = height if sumbu_y < 0 else height - sumbu_y

    region = original_img[top:bottom, left:right]

    left = 0 if sumbu_x < 0 else sumbu_x
    right = width + sumbu_x if sumbu_x < 0 else width

    top = 0 if sumbu_y < 0 else sumbu_y
    bottom = height + sumbu_y if sumbu_y < 0 else height

    new_img[top:bottom, left:right] = region

    return new_img



# Membaca gambar
img = cv.imread('mobil.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "File tidak dapat dibaca"

translasi_x = -20
translasi_y = -40

new_img = translasi(img, translasi_x, translasi_y)

cv.imshow("Hasil", new_img)
cv.waitKey(0)
cv.destroyAllWindows()