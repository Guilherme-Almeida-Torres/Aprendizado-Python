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

pessoa = {
     'nome': 'Guilherme',
     'sobrenome': 'Almeida Torres',
     'idade': 14,
     'altura': 1.72,
     'endereços': [
         {'rua': 'tal tal', 'número': 123},
         {'rua': 'outra rua', 'número': 321},
     ]
 }

for info in pessoa:
    print(info,'|', pessoa[info])
