def second_largest(lista):
    if len(lista) < 2:
        return None
    maior = segundo_maior = float('-inf')
    for num in lista:
        if num > segundo_maior:
            if num >= maior:
                maior, segundo_maior = num, maior            
            else:
                segundo_maior = num
    print(segundo_maior)

lista = [1,2,4,53,6,8,49,12,22,40,42,11]
second_largest(lista)