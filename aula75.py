# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
mult = 1
while mult < 4:

    def multiplicar(y):
        dupli = y * mult
        return dupli
    mult += 1
    resposta = multiplicar(4)
    print(resposta)