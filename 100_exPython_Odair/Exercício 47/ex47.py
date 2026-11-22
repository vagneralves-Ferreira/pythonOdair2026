soma = 0.0
quantidade = 0

for i in range(10):
    nota = float(input(f"Nota {i + 1}: "))
    soma += nota
    quantidade += 1

media = soma / quantidade

print()
print(f"Média: {media:.1f}".replace(".", ","))