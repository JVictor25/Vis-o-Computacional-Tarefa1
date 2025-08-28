arq = open('tabuada.txt', 'w')

def formataMult(x, y):
    z = x * y
    with open('tabuada.txt', 'a') as tab:
        tab.write('{} x {} = {}\n'.format(x, y, z))
def limpaArquivo(nome_arquivo):
    with open(nome_arquivo, 'w') as f:
      return

def createTabuada():
  limpaArquivo('tabuada.txt')
  for j in range(1,10):
    for i in range(1,10):
      formataMult(j, i)
    with open('tabuada.txt', 'a') as tab:
        tab.write('\n')

createTabuada()

arq.close()
