preco = float(input("Preço: R$ ").replace(',', '.'))
opcao = int(input("Opção: ")) 

# opcao 1 - dinheiro ou pix / opcao 2 - debito / opcao 3 - credito a vista / opcao 4 - credito parcelado

if opcao == 1:
    valor_final = preco * 0.90
elif opcao == 2:
    valor_final = preco * 0.95
elif opcao == 3:
    valor_final = preco
elif opcao == 4:
    valor_final = preco * 1.08
else:
    print("\nOpção inválida!")
    valor_final = preco

print(f"\nValor final: R$ {valor_final:.2f}".replace('.', ','))

input("\nPressione Enter para sair...")

