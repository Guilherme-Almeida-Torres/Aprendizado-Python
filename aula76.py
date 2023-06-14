# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
'''
pessoa = {
    'nome' : 'Guilherme',
    'sobrenome' : 'Torres',
    'idade' : 14
}
'''
# print(len(pessoa)) | retorna a quantidade de chaves
# print(pessoa.keys()) | retorna um dict_keys (nome das chaves mais feio)
# print(list(pessoa.keys())[0]) | mostra as o nome das chaves convertido para lista
# print(pessoa['idade'])
'''
import copy
d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [1, 2, 3]
}

#d2 = d1.copy() .copy() serve para tornar um dicionario endependente do outro (apenas valores imutaveis, mutaveis serão linkados)

d2 = copy.deepcopy(d1)
d2['c1'] = 1000
d2['l1'] = 999999
print(d1)
print(d2)
'''

p1 = {
    'nome' : 'Guilherme',
    'sobrenome' : 'Almeida'
}
# print(p1['nome']) serve para a mesma coisa da de baixo
# print(p1.get('nome', 'Não existe'))  .get(nome da chave ) serve para mostrar o valor da chave
'''
nome = p1.pop('nome') #serve para remover um valor do dicionario e salvar ele na variavel
print(nome)
print(p1)
'''
# sobrenome = p1.popitem() inverte a ordem
# print(sobrenome)
# print(p1)

p1.update({ # Serve para atualizar uma lista
    'nome' : 'jose',
    'idade' : 18
}
)
print(p1)