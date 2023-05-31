# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*args): # empacota os numeros
    total = 1
    for numero in args: # Desenpacota os números
        total*= numero # Multiplica os números e coloca dentro de total
    return total

multiplicar = multiplicacao(10, 2, 3, 4, 5)
print(multiplicar)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(x):
    conta = x % 2 
    n1 = x
    if conta == 0:
        print(f'O número {n1} é par')

    else:
        print(f'O número {n1} é impar')

par_impar(5)
 
