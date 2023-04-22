"""
Introdução ao try/except
try -> tentar executar o código
exceto -> ocorreu algum erro ao tentar executar
"""

numero = input('Digite um numero: ')

try:
    print('STR:', numero)
    numero_float = float(numero) # Ocorre um erro aqui, ele pula direto para 
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2 :.2f}')
except:
    print('Este valor não é um número inteiro') # Direto para aqui

#if numero.isdigit():
#    numero_float = float(numero)
#    print(f'O dobro de {numero} é {numero_float * 2 :.2f}')

#else:
#    print('Este valor não é um número inteiro')