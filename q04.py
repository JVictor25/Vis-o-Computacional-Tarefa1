import numpy as np
import sys

if (len(sys.argv) != 4):
  sys.exit(1)

h = int(sys.argv[1])
w = int(sys.argv[2])
x = int(sys.argv[3])


matriz=np.full((h,w),x)

print(matriz)