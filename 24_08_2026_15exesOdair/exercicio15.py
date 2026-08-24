preco_unitario = float(input("Preço unitário: "))
quantidade = float(input("Quantidade: "))
frete = float(input("Frete: "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print(f"\nSubtotal: {subtotal:.2f}")
print(f"Total: {total:.2f}")

