#arquivo = open('./in.txt','r').read().split()

def buscaConjuntos(arquivo):
    lista = open(arquivo,'r').read().split()
    print(formataConjunto(lista[1:int(lista[0])*2+1]))

def formataConjunto(dominos):
    i = 0
    arrayDominos = []
    while i < len(dominos):
        arrayDominos.append([int(dominos[i]), int(dominos[i+1])])
        i+=2
    return arrayDominos

buscaConjuntos('./in.txt')