# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
#print(a, b)

pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Souza'
}

# Formas de desenpaotar um dicionario
'''
(a1, a2), (b1, b2) = pessoa.items() # Quando está sem o values ele mostra apenas as chves e com ele mostra o valor das chaves
print(a1, a2)
print(b1, b2)

print()

a, b = pessoa.values()
print(a, b)

print()

for chave, valor in pessoa.items():
    print(chave, valor)
'''

pessoa = {
    'nome' : 'Ketlyn',
    'sobrenome' : 'Beatriz'
}

dados_pessoa = {
    'idade' : 15,
    'altura' : 1.65,
    }

pessoa_completa = {**pessoa, **dados_pessoa}

for nome, sobrenome in pessoa_completa.items():
    print(nome, sobrenome)

print(pessoa, dados_pessoa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

print()

def mostrar_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_argumentos_nomeados(nome='Guilherme', sobrenome='Almeida', idade=14, altura=1.71)
