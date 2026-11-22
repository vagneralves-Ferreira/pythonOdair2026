vetor = []

print("Vetor:")
for i in range(10):
    valor = float(input().replace(",", "."))
    vetor.append(valor)

soma = 0.0
for valor in vetor:
    soma += valor

print()
print(f"Soma: {soma:g}".replace(".", ","))