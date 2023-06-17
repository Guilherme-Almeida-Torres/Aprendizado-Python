# Uma das funções do set no codigo é retirar valores repetidos sem precisar de nada

s1 = set()
s1 = {1, 2, 3, 3, 1}
print(s1)


l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l2)


s1 = {1, 2, 3}
s1.add('Guilherme')
print(s1)
s1.update(('casa', 4, 5)) # Colocar virgula no final para deixar tudo junto
print(s1)
s1.discard('casa') # Serve para excluir um valor colocando o proprio valor entre parenteses
print(s1)


s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2 # Serve para unir os dois sets
print(s3)

s3 = s1 & s2 # Serve para mostrar os itens presentes no dois
print(s3)

s3 = s1 - s2 # Serve para mostrar somente os intens presentes no set da esquerda
print(s3)

s3 = s1 ^ s2 # Serve para mostrar somente o item que existe em ambos mas não no mesmo
print(s3)