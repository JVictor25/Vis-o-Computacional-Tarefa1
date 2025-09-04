import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt


imagem1 = cv2.imread('patch01.jpg')
imagem2 = cv2.imread('patch02.jpg')
imagem3 = cv2.imread('patch03.jpg')
imagem4 = cv2.imread('patch04.jpg')

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))


axes[0, 0].imshow(imagem1)
axes[1, 0].imshow(imagem2)
axes[0, 1].imshow(imagem3)
axes[1, 1].imshow(imagem4)

fig.savefig('q08.png')

imagemrgb1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2RGB)
imagemrgb2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2RGB)
imagemrgb3 = cv2.cvtColor(imagem3, cv2.COLOR_BGR2RGB)
imagemrgb4 = cv2.cvtColor(imagem4, cv2.COLOR_BGR2RGB)

fig_rgb, axes_rgb = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))


axes_rgb[0, 0].imshow(imagemrgb1)
axes_rgb[1, 0].imshow(imagemrgb2)
axes_rgb[0, 1].imshow(imagemrgb3)
axes_rgb[1, 1].imshow(imagemrgb4)



fig_rgb.savefig('q08rgb.png')