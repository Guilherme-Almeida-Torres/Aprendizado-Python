#Interando Strings com while

nome = 'Guilherme'
tamanho_nome = len(nome)

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)









'''while nome:

    asterisco = '*'
    nome_aste = asterisco + nome[0] + asterisco + nome[1] + asterisco+ nome[2] + asterisco + nome[3] + asterisco + nome[4] + asterisco
    #print(nome[0] + asterisco + )
    print(nome_aste)
    break'''