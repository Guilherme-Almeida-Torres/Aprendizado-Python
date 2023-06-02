"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)# Nessa parte da função tem que ter o *

v = executa(saudacao, 'Bom dia', 'Guilherme')
print(v)