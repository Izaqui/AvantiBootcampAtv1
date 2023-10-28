def primos(lista):
    tamanho = len(lista)
    listprimos =[[]]
    for item in range(tamanho):
        init = 0
        num = lista[item]
        total_Div = 0
        for c in range(1,num + 1):
            if num % c == 0:
                total_Div += 1
        if total_Div == 2:
            listprimos[init].append(num)
            init += 1
    print('Lista de Numeros Primos')
    print(listprimos)

lista = [1,2,8,5,7,14,54,84,3,878,45,88,22,25,45,56]
primos(lista)