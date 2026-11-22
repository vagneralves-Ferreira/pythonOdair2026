matriz = []

print("Entrada:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)

print()
print("Matriz:")
for i in range(3):
    for j in range(3):
        fim = " " if j < 2 else ""
        print(matriz[i][j], end=fim)
    print()