matriz = []

print("Matriz:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input().replace(",", "."))
        linha.append(valor)
    matriz.append(linha)

soma = 0.0
for i in range(3):
    for j in range(3):
        soma += matriz[i][j]

print()
print(f"Soma: {soma:g}".replace(".", ","))