#metodo buscar todos conjuntos
def buscarTodosConjuntos(lista, indexQtdDominos):
    buscando = True
    listaConjuntos = []
    while buscando:
        if lista[indexQtdDominos] != '0':
            listaConjuntos.append(buscarProximoConjunto(lista,indexQtdDominos))


            indexQtdDominos = int(lista[indexQtdDominos]) * 2+1+indexQtdDominos

        else:
            buscando =False

    return listaConjuntos

def buscarProximoConjunto(lista, indexQtdDominos):
    list = formataConjunto(lista[indexQtdDominos+1:indexQtdDominos+int(lista[indexQtdDominos]) * 2 + 1])
    return list

def formataConjunto(dominos):
    i = 0
    arrayDominos = []
    while i < len(dominos):
        arrayDominos.append([int(dominos[i]), int(dominos[i + 1])])
        i += 2
    return arrayDominos

    #indexQtdDominos = int(lista[indexQtdDominos]) +1
    primeiroDominoConjunto = indexQtdDominos+1
    #formataConjunto(lista[1:int(lista[0]) * 2 + 1])

def buscaConjuntos(arquivo):
    lista = open(arquivo,'r').read().split()
    listX = buscarTodosConjuntos(lista,0)
    print(listX[0])
    soma(listX[0])

#metodo soma
def soma(lista):
    somaSuperior = 0
    somaInferior = 0
    for conjunto in lista:
        somaSuperior += conjunto[0]
        somaInferior += conjunto[1]
    print(str(somaSuperior)+' - '+str(somaInferior))

buscaConjuntos('./in.txt')