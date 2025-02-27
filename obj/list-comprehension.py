lista1 = [x for x in range(10) if x < 5]
print(lista1)

lista_frutas = ["Melancia", "Maçã", "Abacaxi", "cereja"]

#variavel, for, variavel, in onde, se
nova_lista=[x for x in lista_frutas if "M" in x]
print(nova_lista)

#dict_comprehention
dict_alunos= {'bob': 10, 'airton':6, 'ana': 7}

dict_alunos_info = {k:v for (k,v) in dict_alunos.items()}
print(dict_alunos_info)

dict_alunos_situcao = {k: ('Aprovado' if v > 6 else 'Reprovado') for (k,v)in dict_alunos.items()}
print(dict_alunos_situcao)