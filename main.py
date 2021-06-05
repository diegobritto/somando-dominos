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
    #print(listX[0])
    #print(validarSoma(listX[0], 0))
    for item in listX:

        retorno = soma(item)
        print(retorno)
#        if retorno[0] != retorno[1]:
#            print("impossivel")
#        else:
#            print(retorno)

#metodo soma
def soma(lista):
    somaMenores = 0
    somaMaiores = 0
    encontrouDiferenca = False
    for conjunto in lista:
        somaMenores += min(conjunto)
        somaMaiores += max(conjunto)
    diferenca = (somaMaiores - somaMenores)/2
    return somaMaiores, somaMenores, diferenca


'''def somaMestre(lista):
    sumLeft = 0
    sumRight = 0
    auxList = []    
    for item in lista:
        if len(auxList) == 0:
            print(item)
            if item[0]<item[1]:                        
                sumLeft = item[0]
                sumRight = item[1]
                auxList.append((max(item)-min(item)))
            else:
                sumLeft = item[1]
                sumRight = item[0]
                auxList.append((max(item)-min(item)))
        else:
            
           # print(item,(sumLeft) , (sumRight))                     
            if (item[0]<item[1] and sumRight<=sumLeft) or (item[0]>item[1] and sumLeft<=sumRight):
                print(3,item, sumLeft,sumRight)
                sumLeft = item[0]+sumLeft
                sumRight = item[1]+sumRight
                auxList.append((max(item)-min(item)))
            else:                
                print(4,item, sumLeft,sumRight)
                sumLeft = item[1]+sumLeft
                sumRight = item[0]+sumRight
                auxList.append((max(item)-min(item)))
    #print(sumLeft, sumRight)
    if sumLeft!= sumRight:
       # print(lista)
        diferenca  =(max(sumLeft,sumRight)-min(sumLeft,sumRight))
        if diferenca in auxList:



            item = lista[auxList.index(diferenca)]        
            a= max(sumLeft,sumRight)-max(item)
            b = min(sumLeft,sumRight)-min(item)
            sumLeft=a
            sumRight =b

    return sumLeft,sumRight'''




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

buscaConjuntos('./in2.txt')