# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7 8
#  G u i l h e r m e
# -9-8-7-6-5-4-3-2-1

nome = 'Guilherme'
# print(nome[2])
# print(nome[-7])
# print('Gui' in nome)# Isso está entre nome
# print('z' in nome)
# print(10 * '-')
# print('Gui' not in nome)# Isso não está entre nome
# print('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja buscar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')