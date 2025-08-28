import sys

def createSeq(n):
  seq = [n]
  while n != 1:
    if(n%2==0):
      n=n/2
      seq.append(n)
    else:
      n=(3*n)+1
      seq.append(n)
  return seq

if len(sys.argv) != 2:
  sys.exit(1) 
numero_inicial_str = sys.argv[1]

numero_inicial_int = int(numero_inicial_str)
sequencia = createSeq(numero_inicial_int)
print(sequencia)
