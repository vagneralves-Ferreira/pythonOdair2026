quantidade = 0
total = 0.0
maior_preco = 0.0

while True:
    preco = float(input("Preço: ").replace(",", "."))
    if preco == 0:
        break
    quantidade += 1
    total += preco
    if quantidade == 1 or preco > maior_preco:
        maior_preco = preco

print()

if quantidade == 0:
    print("NENHUM PRODUTO INFORMADO")
else:
    print(f"Produtos: {quantidade}")
    print(f"Total: R$ {total:.2f}".replace(".", ","))
    print(f"Maior preço: R$ {maior_preco:.2f}".replace(".", ","))