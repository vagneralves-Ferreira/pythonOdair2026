matriz = []

print("Matriz:")
for i in range(4):
    linha = []
    for j in range(4):
        valor = float(input().replace(",", "."))
        linha.append(valor)
    matriz.append(linha)

maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print()
print(f"Maior valor: {maior:g}".replace(".", ","))
print(f"Primeira posição: linha {linha_maior}, coluna {coluna_maior}")