import random


for _ in range(100):
    nove_digitos = ""
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    cont_regressivo = 10
    result_digito1 = 0
    for digito in nove_digitos:
        result_digito1 += int(digito) * cont_regressivo
        cont_regressivo -= 1
    digito1 = (result_digito1 * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0

    # Calculo para segundo digito, pega o resulta do for anterior e joga neste abaixoCurso Básico Pyhton, Lógica
    cont_regressivo2 = 0
    dez_digitos = nove_digitos + str(digito1)
    result_digito2 = 0
    for digito2 in dez_digitos:
        result_digito2 += int(digito2) * cont_regressivo2
        cont_regressivo2 -= 1
    digito2 = (result_digito2 * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0

    cpf_gerado = f"{nove_digitos}{digito1}{digito2}"

    print(f"CPF: {cpf_gerado}")