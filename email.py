email="mestre@gmail.com"
email2= "jorge-amado@outlook.com"

#pegar o servidor dos emails
posicao_arroba = email.find("@")+1
servidor = email[posicao_arroba:]
print(servidor)
