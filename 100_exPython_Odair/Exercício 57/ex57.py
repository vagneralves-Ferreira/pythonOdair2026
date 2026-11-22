quantidade = 0
soma = 0.0

while True:
    valor = float(input("Valor: ").replace(",", "."))
    if valor == 0:
        break
    quantidade += 1
    soma += valor

print()

if quantidade == 0:
    print("NENHUM VALOR VÁLIDO")
else:
    media = soma / quantidade
    print(f"Quantidade: {quantidade}")
    print(f"Soma: {soma:g}".replace(".", ","))
    print(f"Média: {media:g}".replace(".", ","))