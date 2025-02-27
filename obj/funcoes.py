def primeiraFunc():
    nome = 'Gabriel'
    print(f'hello{nome}')

primeiraFunc()

#o * espera um valor indeterminado de objetos
def printVarInfo(arg, *vartuple):
    print("argumento:",arg)
    for item in vartuple:
        print("parametro: ",item)
    return;

printVarInfo('var', 'asas', 'mouse', 'lactos')