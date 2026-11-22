preco = float(input("Preço do produto: R$ "))

opcao = int(input("Opção de pagamento (1-4): "))

if opcao == 1:
    print(f"Dinheiro ou Pix: R$ {preco - (preco * 10 / 100):.2f}")  

elif opcao == 2:
    print(f"Débito: R$ {preco - (preco * 5 / 100):.2f}")

elif opcao == 3:    
    print(f"Crédito à vista: R$ {preco:.2f}")

elif opcao == 4:
    print(f"Crédito parcelado: R$ {preco + (preco * 8 / 100):.2f}")
else:
    print("Opção inválida")

input("Pressione ENTER para sair...")
