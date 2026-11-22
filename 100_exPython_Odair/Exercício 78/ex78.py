matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input().replace(",", "."))
        linha.append(valor)
    matriz.append(linha)

diagonal = []
soma = 0.0

for i in range(3):
    elemento = matriz[i][i]
    diagonal.append(elemento)
    soma += elemento

print()
print("Diagonal principal:", end=" ")
for i in range(3):
    fim = " " if i < 2 else ""
    print(f"{diagonal[i]:g}".replace(".", ","), end=fim)

print()
print(f"Soma: {soma:g}".replace(".", ","))