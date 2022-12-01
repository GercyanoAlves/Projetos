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
    sair = input("Digite -1 para Sair ou ENTER para continuar: \n")
    if sair == '-1':
        break
    itens.append(input("Nome do produto: "))
    qtd = float(input('Quantidade: '))
    preco = float(input("Preco do produto: "))
    total_preco.append(float(qtd*preco))
    
    print("Total R$ %.2f"%total_preco[y])
    print()
    y += 1

    
print("Valor total da compra é de R$%.2f"%sum(total_preco))

print("###############################################")
print("###############################################")
print("###############################################")
print("###############################################")
print("###############################################")
