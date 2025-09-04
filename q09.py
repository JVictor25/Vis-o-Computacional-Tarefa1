import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt

imagem = cv2.imread('patch01.jpg')

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

bordas = cv2.Canny(imagem_cinza, 100, 200)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 8))

axes[0].imshow(imagem)
axes[1].imshow(bordas)

fig.savefig('q09.png')