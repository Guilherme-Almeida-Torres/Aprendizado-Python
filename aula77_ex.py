import emoji


print('(escolha entre a, b, c ou d) \nResponda a pergunta: ')
print('Quanto é 4 x 2 ?')
print('a) 8 \nb) 2 \nc) 14 \nd) 22')
questão_1 = input('Escolha uma opção: ').lower()

i = 0 
if questão_1 == 'a' or questão_1 == '8':
    print(emoji.emojize('Certo! :thumbs_up:'))
    i += 1

else:
    print('Errou')
print('')


print('Qual o estado brasileiro que pediu independencia de Portugal?')
print('a)Bahia \nb)Pernambuco \nc)Minas Gerais \nd)Espirito Santo')
questão_2 = input('Escolha uma opção: ').lower()

if questão_2 == 'c' or questão_2 == 'minas gerais':
    print(emoji.emojize('Certo! :thumbs_up:'))
    i += 1

else:
    print('Errou')
print('')


print('Qual o nome do cantor Fabio Jr')
print('a)José \nb)Roberto \nc)Jaime \nd)Fabio')
questão_3 = input('Escolha uma opção: ').lower()

if questão_3 == 'd' or questão_3 == 'fabio':
    print(emoji.emojize('Certo! :thumbs_up:'))
    i += 1

else:
    print('Errou')
print('')

print(f'Você acertou {i} questões!')
print('')