primeiroV = input('Digite um valor: ')
segundoV = input('Digite outro valor: ')

if primeiroV > segundoV:
    print(f'O primeiro valor ({primeiroV}) é maior que o segundo valor ({segundoV})')

elif primeiroV == segundoV:
    print(f'Os valores {primeiroV} e {segundoV} são iguais')

elif segundoV > primeiroV:
    print(f'O segundo valor ({segundoV}) é maior que o primeiro valor ({primeiroV})')

else:
    print('Nenhum valor foi digitado')
    print('.exit()')
