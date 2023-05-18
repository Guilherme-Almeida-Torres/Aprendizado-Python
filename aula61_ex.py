cpf = '74682489070'
cpf_9_digitos = cpf[0:9]
contador_regressivo = 10

resultado_digito_1 = 0
for digito_1 in cpf_9_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo
    contador_regressivo -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)