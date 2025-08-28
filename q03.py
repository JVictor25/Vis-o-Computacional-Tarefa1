import sys

def fatorial(n):
    fat=1
    for i in range(1,n+1):
        fat=i*fat
    return fat

def coefBinomial(a, b):
    return fatorial(a)/(fatorial(b)*fatorial(a-b))

if (len(sys.argv) != 3):
  sys.exit(1)

n = int(sys.argv[1])
k = int(sys.argv[2])

if(n<=k):
    sys.exit(1)

result=coefBinomial(n,k)
print(result)
