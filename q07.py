import numpy as np
import sys
import matplotlib.pyplot as plt

h = 200
w = 280

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))

matrizCinza=np.tile(127,(h,w))

axes[0, 0].imshow(matrizCinza, cmap='gray', vmin=0, vmax=255)
axes[0, 0].set_title('Cinza')


matrizBranca=np.tile(255,(h,w))

axes[0, 1].imshow(matrizBranca, cmap='gray', vmin=0, vmax=255)
axes[0, 1].set_title('Branca')

linha=[]

for i in range(4):
    for j in range(30):
        linha.append(255)
    for j in range(30):
        linha.append(0)
for j in range(30):
    linha.append(255)
for j in range(10):
    linha.append(0)

matrizVerticais=np.tile(linha,(h,1))

axes[0, 2].imshow(matrizVerticais, cmap='gray', vmin=0, vmax=255)

axes[0, 2].set_title('Verticais')

linhaBranca=np.tile(255,(30,w))
linhaPreta=np.tile(0,(30,w))
linhas=np.vstack((linhaBranca, linhaPreta))

matrizHorizontais=np.tile(linhas,(3,1))

linhaBranca=np.tile(255,(20,w))
matrizHorizontais=np.vstack((matrizHorizontais,linhaBranca))

axes[1, 0].imshow(matrizHorizontais, cmap='gray', vmin=0, vmax=255)
axes[1, 0].set_title('Horizontais')

casaBranca=np.tile(255,(30,30))
casaPreta=np.tile(0,(30,30))

casasV1=np.hstack((casaPreta, casaBranca))
casasV2=np.hstack((casaBranca, casaPreta))

casas=np.vstack((casasV1,casasV2))

matrizXadrez=np.tile(casas,(3,4))

casaBranca=np.tile(255,(20,30))
casaPreta=np.tile(0,(20,30))

casasV1=np.hstack((casaPreta, casaBranca))
casas=np.tile(casasV1,(1,4))
matrizXadrez=np.vstack((matrizXadrez,casas))

casaBranca=np.tile(255,(30,10))
casaPreta=np.tile(0,(30,30))
casasV1=np.hstack((casaPreta, casaBranca))

casaBranca=np.tile(255,(30,30))
casaPreta=np.tile(0,(30,10))
casasV2=np.hstack((casaBranca, casaPreta))

casas=np.vstack((casasV1,casasV2))
casas=np.tile(casas,(3,1))

casaBranca=np.tile(255,(20,10))
casaPreta=np.tile(0,(20,30))
casasV1=np.hstack((casaPreta, casaBranca))
casas=np.vstack((casas,casasV1))
matrizXadrez=np.hstack((matrizXadrez,casas))


axes[1, 1].imshow(matrizXadrez, cmap='gray', vmin=0, vmax=255)
axes[1, 1].set_title('Xadrez')

#imagem com intensidades aleatórias entre 0 e 255 (utilize np.random.randint)
matrizAleatoria = np.random.randint(0, 256, size=(h, w))

axes[1, 2].imshow(matrizAleatoria, cmap='gray', vmin=0, vmax=255)

axes[1, 2].set_title('Aleatoria')

fig.savefig('q07.png')