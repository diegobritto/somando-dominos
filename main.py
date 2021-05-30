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
#    print(listX[0])
    print(validarSoma(listX[0], 0))

#metodo soma
def soma(lista):
    somaSuperior = 0
    somaInferior = 0
    for conjunto in lista:
        somaSuperior += conjunto[0]
        somaInferior += conjunto[1]
    return (somaSuperior, somaInferior)

def validarSoma(lista, dominoExcluido):
    x = soma(lista)
    if (min(x) == max(x)):
        return (x, dominoExcluido)
    elif (max(x)-min(x) > 1):
        inverterDomino(lista, lista.index(dominoMaiorSoma(lista)))
        x = validarSoma(lista, dominoExcluido)
    else:
        dominoExcluido = str(dominoMenorSoma(lista))
        excluirDomino(lista, lista.index(dominoMenorSoma(lista)))
        print(dominoExcluido)
        x = validarSoma(lista, dominoExcluido)      
    return (x, dominoExcluido)
#    print(min(lista))

def inverterDomino(lista, index):
    aux = lista[index][0]
    lista[index][0] = lista[index][1]
    lista[index][1] = aux

def excluirDomino(lista, index):
    dominoExcluido = lista[index]
    lista[index][0] = 0
    lista[index][1] = 0
    return dominoExcluido

def dominoMaiorSoma(lista):
    maior = [0, 0]
    for x in lista:
        if x[0] + x[1] > maior[0] + maior[1]:
            maior = x
    return maior

def dominoMenorSoma(lista):
    menor = [1000, 1000]
    for x in lista:
        if x[0] + x[1] < menor[0] + menor[1]:
            menor = x
    return menor

buscaConjuntos('./in.txt')