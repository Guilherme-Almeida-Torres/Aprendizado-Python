# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
'''
lista = [4, 32, 1, 4, 35, 6, 6, 21]
lista.sort() # Serve para colocar os números em ordem crescente
# lista.sort(reverse=True) serve para colocar em ordem decrescente
'''

lista = [
     {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
]
'''
def ordena(item):
    return item['nome']
'''
l1 = sorted(lista, key=lambda item: item ['nome']) # Faz o mesmo do que está em cima
l2 = sorted(lista, key=lambda item: item ['sobrenome'])

for item in lista:
    print(item)