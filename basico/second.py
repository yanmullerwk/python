a=30
b=20

#string integrada com variavel
print(f"a:{a}, b:{b}")

#maiusculo
nome= "marcos avila"
nome = nome.upper()
print(f"nome maiusculo:{nome}")

#minusculo
nome = nome.lower()
print(f"minusculo:{nome}")

#find
print(nome.find("av"))

#tamanho
print(len(nome))

#selecionar elementos
print(nome[0], nome[1], nome[2], nome[3],nome[4])

print(nome[-4])

#pega a partir de determinada poição
print(nome[:5])
#intervalo
print(nome[1:4])

#REPLACE

novonome=nome.replace("marcos","mike")
print(novonome)

outro_nome="joao miller"
print(outro_nome.capitalize())#primeira letra maiuscula
print(outro_nome.title())#primeira letra de cada palavra maiuscula