

def calcula_imposto(vendas):
    imposto_total = 0
    for preco in vendas:
        if preco > 1000:
            taxa = 0.15
        else:
            taxa = 0.1
        imposto = preco*taxa
        imposto_total= imposto_total+imposto
    return imposto_total

lista_precos=[1000, 299, 800, 2000]
imposto_lista1= calcula_imposto(lista_precos)
print(imposto_lista1)