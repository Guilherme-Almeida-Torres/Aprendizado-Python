# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
#print(list(range(10))) #range serve para contar de 0 ate 10
import pprint

def P(x):
    pprint.pprint(x, sort_dicts=False, width=40) # Serve para deixar o print da lista mais bonito

lista = []
for numeros in range(10):
    lista.append(numeros)
#print(lista)

lista = [numeros * 2 for numeros in range(10)]
#print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome' : 'p1', 'preço' : 20,},
    {'nome' : 'p2', 'preço' : 10,},
    {'nome' : 'p3', 'preço' : 30,}
    ]
novos_produtos = [
    {**produto, 'preço' : produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
    ]

# print(novos_produtos)
# P(novos_produtos)
'''
lista = [n for n in range(10) if n <= 5]
print(lista)
'''

novos_produtos = [
    {**produto, 'preço' : produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
    if produto['preço'] >= 20 and produto['preço'] * 1.05 > 10
    ]

P(novos_produtos)