'''Calculadora com while'''

while True:

    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')

    numero_1_int = int(numero_1)
    numero_2_int = int(numero_2)

    if numero_1.isdigit() and numero_2.isdigit():

        pergunta = input('Qual conta vc quer: ').lower()

        if pergunta == 'soma' and pergunta == '+':
            soma = numero_1_int + numero_2_int
            print(f'A soma e de {soma}')

        if pergunta == 'subtração' or pergunta == 'subtracao' or pergunta == 'subitração' or pergunta == 'subitracao' and pergunta == '-':
            subtracao = numero_1_int - numero_2_int
            print(f'A subtração é {subtracao}')

        if pergunta ==  'multiplicacao' or pergunta == 'multiplicação' and pergunta == '*':
            multiplicacao = numero_1_int * numero_2_int
            print(f'A multiplicação é {multiplicacao}')

        if pergunta ==  'divisão' or pergunta == 'divisao' and pergunta == '/':
            divisao = numero_1_int / numero_2_int
            print(f'A divisão é {divisao}')



    print('')
    print('Para continuar aperte [enter]')
    print('')
    sair = input('Para sair digite [s]').lower().startswith('s')
    #print(sair)
    if sair is True:
        break