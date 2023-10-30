def ordenar_pessoa(dicionarioPessoa):
    dicionarioPessoa['nomeIdade'].sort()

    for x in range(len(dicionarioPessoa['nomeIdade'])):
        print(dicionarioPessoa['nomeIdade'][x])

#lista_pessoas
pessoas = [('joaquim',20),('aline',18),('angela',19),('sheldon',31),('leonard',28),('raje',27),('raui',28),('ammy',32)]
#
dicionarioPessoa = {
     'nomeIdade':[('pedro',29),('ana',22),('bruna', 39),('sheldon', 42),('leonard', 19),('zulu', 21)]
}

print('\n ordenar com Sorted\n')
ordem = sorted(pessoas)
print(ordem)
print('\n Orderna com a função')
ordenar_pessoa(dicionarioPessoa)