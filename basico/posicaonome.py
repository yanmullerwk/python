nome = "arthur menger"
acha_espaco = nome.find(" ")
primeiro_nome = nome[:acha_espaco]
print(primeiro_nome)
#quando pega do inicio a te cert posição a ultima nunca é incluida, agr, se pega de uma posição ate o fnal ele inclui
sobrenome = nome[acha_espaco+1:]
print(sobrenome)