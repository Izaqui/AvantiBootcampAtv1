
def criarNewList(lista1,lista2):
    newList=[]
    tmh1 = len(lista1)
    tmh2 = len(lista2)
    posic = 0
    for posic in range(tmh1):
        valor = lista1[posic]
        for num in range(tmh2):
            valor2 = lista2[num]
            if valor == valor2 :
                print(f'esta valor ({valor}) esta pesente em ambas as listas')
                break
            elif valor is not lista2[num] and valor == lista1[num]: 
                    newList.append(lista1[posic])
                    valor = lista1[posic]
                    break
        
    print(newList)



lista1 = [1,2,4,6,7,9,22,113,8,91]
lista2 = [0,3,4,5,12,98,8,144,15,92]

criarNewList(lista1,lista2)