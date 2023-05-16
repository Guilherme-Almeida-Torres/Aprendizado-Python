"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]
# print(salas[2][3][2])  Busca na terceira lista depois do indice 3 que e a tupla depois ele vai no indice dois

for sala in salas:
    print(f'A sala é {sala}')
    for alunos in sala:
        print(alunos)