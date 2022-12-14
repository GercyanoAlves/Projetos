import os
itens = []
preco = []
qtd = []
total_preco = []

y = 0


print("###############################################")
print("###############################################")
print("############## Lista de Compras ###############")
print("###############################################")
print("###############################################\n")

while True:
    opcao = input("Digite sair minusculo para encerrar ou ENTER para continuar: ")
    if opcao == 'sair':
        break
    try:
        itens.append(input("Nome do produto: "))
        qtd = float(input('Quantidade: '))
        preco = float(input("Preco do produto: "))
        total_preco.append(float(qtd*preco))
        
        print("Total R$ %.2f"%total_preco[y])
        print()
        y += 1
    except ValueError:
        os.system("clear")
        print("""\nPara adicionar o produto na lista veja o que é obrigatório.
        1- Produto pode ficar em branco
        2- Colocar quantidade é obrigatoria
        3- Colocar preço é obrigatório
        4- Não pode usar VÍRGULA e tampouco LETRAS\n""")

for indice, compras in enumerate(itens):
    print(indice, compras)
print("Produtos listada acima estão no carrinho")
print("Valor total da compra é de R$%.2f"%sum(total_preco))

print("###############################################")
print("###############################################")
print("###############################################")
print("###############################################")
print("###############################################")
