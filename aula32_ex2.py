entrada = input('Digite a hora em numero inteiro: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')

    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    
    elif hora >=17 and hora <= 23 :
        print('Boa noite!')

    else:
        print(f'Não conheço essa hora {entrada}')

except:
    print(f'Você não digitou um valor valido "{entrada}"')