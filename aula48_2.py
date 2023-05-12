'''
Cuidados com dados mutaveis
= - copiando valor (mutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
'''

lista_a = ['Guilherme', 'Matheus', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'qualquer coisa'

print(lista_b)