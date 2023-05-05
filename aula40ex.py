'''Calculadora com while'''

while True:

    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')

    numero_1_int = float(numero_1)
    numero_2_int = float(numero_2)

    if numero_1.isdigit() and numero_2.isdigit():

        pergunta = input('Qual conta vc quer: ').lower()

        # Parte de somar  
        if pergunta == 'soma' :
            soma = numero_1_int + numero_2_int
            print(f'A soma e de {soma}')
        if pergunta == '+':
            soma = numero_1_int + numero_2_int
            print(f'A soma e de {soma}')

        # Parte de subtração
        if pergunta == 'subtração' or pergunta == 'subtracao' or pergunta == 'subitração' or pergunta == 'subitracao':
            subtracao = numero_1_int - numero_2_int
            print(f'A subtração é {subtracao}')
        if pergunta == '-':
            subtracao = numero_1_int - numero_2_int
            print(f'A subtração é {subtracao}')

        # Parte de multiplicação
        if pergunta ==  'multiplicacao' or pergunta == 'multiplicação':
            multiplicacao = numero_1_int * numero_2_int
            print(f'A multiplicação é {multiplicacao}')
        if pergunta == '*':
            multiplicacao = numero_1_int * numero_2_int
            print(f'A multiplicação é {multiplicacao}')

        # Parte da divisão
        if pergunta ==  'divisão' or pergunta == 'divisao':
            divisao = numero_1_int / numero_2_int
            print(f'A divisão é {divisao}')
        if pergunta == '/':
            divisao = numero_1_int / numero_2_int
            print(f'A divisão é {divisao}')



    print('')
    print('Para continuar aperte [enter]')
    print('')
    sair = input('Para sair digite [s]').lower().startswith('s')
    #print(sair)
    if sair is True:
        break