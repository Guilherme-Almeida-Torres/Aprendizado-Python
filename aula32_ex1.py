entrada = input('Digite um número: ') # Perguta

if entrada.isdigit(): # Retorna um valor booleano
    entrada_int = int(entrada) # Transforma o número em inteiro
    par_impar = entrada_int % 2 == 0 # pega o resultado do resto da divisão por 2 e compara com 0
    par_impar_texto = 'impar' # Mostra par na tela
    
    if par_impar is True:
        par_impar_texto = 'par'
    
    print(f'O número {entrada_int} é {par_impar_texto}')

else:
    print('Você não digitou um numero inteiro')