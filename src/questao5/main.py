def maior_menor(lista):
    maior_valor = 0
    menor_valor = 0

    for x in range(len(lista)):
        if x == 0:
            maior_valor = menor_valor = lista[x]
        else:
            if lista[x] > maior_valor:
                maior_valor = lista[x]
            if lista[x] < menor_valor:
                menor_valor = lista[x]


    print(f'o maior valor é {maior_valor}')
    print(f'o menor valor é{menor_valor}')

lista = [1,2,8,5,7,14,54,0,84,3,878,45,88,22,25,45,56]

maior = max(lista)
menor = min(lista)
print('lista\n')
print(lista)
print('\nMaior numero:',maior,' .usando a (max)')
print('\nMenor nuemro:',menor,' .usando a (min)')
print('\n usando a função\n')
maior_menor(lista)