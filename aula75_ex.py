# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
mult = 1
while mult < 4: # Serve para executar até o multiplicador der 4

    def multiplicar(y): # Função para multiplicar
        dupli = y * mult
        return dupli
    mult += 1 # Almenta o multiplicador
    resposta = multiplicar(4) # Gravo a função e dou um numero para ele multiplicar
    print(resposta)  # Mostra resposta
