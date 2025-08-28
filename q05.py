import numpy as np
import sys

if (len(sys.argv) != 3):
  sys.exit(1)

h = int(sys.argv[1])
w = int(sys.argv[2])

linha=np.array(range(w))

matriz=np.tile(linha,(h,1))

print(matriz)