matriz = []

print("Matriz:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input().replace(",", "."))
        linha.append(valor)
    matriz.append(linha)

somas_linhas = []
for i in range(3):
    soma_l = 0.0
    for j in range(3):
        soma_l += matriz[i][j]
    somas_linhas.append(soma_l)

somas_colunas = []
for j in range(3):
    soma_c = 0.0
    for i in range(3):
        soma_c += matriz[i][j]
    somas_colunas.append(soma_c)

print()
print("Somas das linhas:", end=" ")
for i in range(3):
    separador = ", " if i < 2 else ""
    print(f"{somas_linhas[i]:g}".replace(".", ","), end=separador)

print()
print("Somas das colunas:", end=" ")
for j in range(3):
    separador = ", " if j < 2 else ""
    print(f"{somas_colunas[j]:g}".replace(".", ","), end=separador)
print()