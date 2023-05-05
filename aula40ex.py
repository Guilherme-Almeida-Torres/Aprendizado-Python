'''Calculadora com while'''

while True:

    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    pergunta = input('Qual conta vc quer: ').lower()

    numeros_validos = None
    
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou os dois valores digitados são invalidos')
        print("\n")
        continue


    # Parte de somar  
    elif pergunta == 'soma' :
            soma = numero_1_float + numero_2_float
            print(f'A soma é de {soma}')
    elif pergunta == '+':
            soma = numero_1_float + numero_2_float
            print(f'A soma é de {soma}')

    # Parte de subtração
    elif pergunta == 'subtração' or pergunta == 'subtracao' or pergunta == 'subitração' or pergunta == 'subitracao':
            subtracao = numero_1_float - numero_2_float
            print(f'A subtração é {subtracao}')
    elif pergunta == '-':
            subtracao = numero_1_float - numero_2_float
            print(f'A subtração é {subtracao}')

    # Parte de multiplicação
    elif pergunta ==  'multiplicacao' or pergunta == 'multiplicação':
            multiplicacao = numero_1_float * numero_2_float
            print(f'A multiplicação é {multiplicacao}')
    elif pergunta == '*':
            multiplicacao = numero_1_float * numero_2_float
            print(f'A multiplicação é {multiplicacao}')

    # Parte da divisão
    elif pergunta ==  'divisão' or pergunta == 'divisao':
            divisao = numero_1_float / numero_2_float
            print(f'A divisão é {divisao}')
    elif pergunta == '/':
            divisao = numero_1_float / numero_2_float
            print(f'A divisão é {divisao}')



    print('')
    print('Para continuar aperte [enter]')
    print('')
    sair = input('Para sair digite [s]').lower().startswith('s')

    if sair is True:
        break
