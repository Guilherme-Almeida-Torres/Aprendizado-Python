# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave.upper(): valor.upper()
    if isinstance(valor, str) and isinstance(chave, str) else valor
    for chave, valor in produto.items()
}

print(dc)