arquivo = open('C:/Users/I532134/OneDrive - SAP SE/Facul/Análise e Projeto de Algoritmos/Trabalho Grau B/in.txt','r')
qtdDominos = int(arquivo.readline())

while qtdDominos != 0:
    i = 0
    arrayDominos = [[0, 0]]*qtdDominos
    while i < qtdDominos:
        domino = arquivo.readline()
        domino = domino.split()
        arrayDominos[i][0] = domino[0]
        arrayDominos[i][1] = domino[1]
        print(arrayDominos[i][0])
        print(arrayDominos[i][1])
        i+=1
    break

print(arrayDominos[0][0])
print(arrayDominos[0][1])
print(arrayDominos[1][0])
print(arrayDominos[1][1])
print(arrayDominos[2][0])
print(arrayDominos[2][1])