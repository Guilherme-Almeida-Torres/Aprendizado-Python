import time
import sys
import os

while True:

    def error_zero_division(x, y):
    
        try:
            x / y
        
        except ZeroDivisionError:
            print('Não ha como dividir por zero')
            
            
        
    def division(x, y):
    
        error_zero_division(y, x)
        return x // y
        
    def multiplication(x, y):
    
        return x * y
        
    def sum(x, y):
        
        return x + y
        
    def subtraction(x, y): 

        return x - y

    new_number_1 = int(input('Digite um número: '))
    new_number_2 = int(input('Digite outro número: '))


    print(f'Qual operação matematica você deseja realizar com os números {new_number_1} e {new_number_2}?')

    #time.sleep(2)

    print('Para somar digite [S] \nPara subtrair digite [SUB] \nPara multiplicar digite [M] \nPara dividir digite [D]')

    #time.sleep(2)

    what_math = str(input('Qual será a operação: '))

    if what_math == "S" or what_math == "s":
        print(sum(new_number_1, new_number_2))

    elif what_math == "SUB" or what_math == "sub":
        print(subtraction(new_number_1, new_number_2))

    elif what_math == "M" or what_math == "m":
        print(multiplication(new_number_1, new_number_2))

    elif what_math == "D" or what_math == "d":
        print(division(new_number_1, new_number_2))

    question = input('Você quer continuar? digite [S] ou [N]: ')

    if question == 'n' or question == 'N':
        os.system('cls') # <-- Quero linpar a linha de comando aqui
        break
    
    if question == "s" or question == 'S':
        os.system('cls')