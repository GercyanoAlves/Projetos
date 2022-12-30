import os
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

# Desempacotamento das perguntas em for
for pergunta in perguntas:
    print("Pergunta:",pergunta["Pergunta"])
    print()

    # Desempacotamento das respostas em for com enumerate 
    opcoes = pergunta["Opções"]
    for i,opcao in enumerate(opcoes):
        print(f"{i})", opcao)
    print()
    escolha = input("Escolha uma opção: ")
    os.system("clear")

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    # Só serão aceito números
    if escolha.isdigit():
        escolha_int = int(escolha)

    # Condições para saber se a resposta está correta
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        acertos += 1
        print("Acertou 👏👍")
    
    else:
        print("Errou 😔❌")

print("Vc acertou", acertos)
print("de", len(perguntas), "perguntas.")