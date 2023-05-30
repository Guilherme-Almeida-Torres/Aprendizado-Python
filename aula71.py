'''
args - argumentos não nomeados 
* - *args (empacotamento e desenpacotamento)
Lembre-se de desenpacota
'''
#x, y, *resto = 1, 2, 3, 4
#print(x, y, resto)

#def soma(x ,y):
#    return x + y

def soma(*args):
    #args = list(args) args e uma tupla isso serve para transformar em list
    total = 0
    for numero in args:        
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)

print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)

print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 100
outra_soma = soma(*numeros) # Neste caso o asterisco serve para desenpacotar a tupla
print(outra_soma)