vendas = [1000, 20, 400, 333, 90, 160, 435, 74, 35]

#for i in vendas:
 #   if i > 1000:
  #      taxa = 0.1
   # else:
    #    taxa = 0.15
    #mposto = taxa*i
    #print(f"preço: {i} imposto: {imposto}")


vendas_23 ={"jan": 15000, "fev": 10000, "mar": 5000}
vendas_24 ={"jan": 16000, "fev": 20000, "mar": 4000}

for mes in vendas_24:
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]
    crescimento = valor_24/valor_23 - 1
    print(f"No mês de {mes} o crescimento foi de {crescimento: .1%}")
