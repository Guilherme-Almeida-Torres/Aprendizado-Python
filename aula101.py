# Exercício - Adiando execução de funções
def soma(y):
    x = 5
    return x + y


def multiplica(y):
    x = 10
    return x * y


def criar_funcao(funcao, y):
    return funcao(y)


soma_com_cinco = criar_funcao(soma, 10)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco, multiplica_por_dez, sep='\n')
