vetor_a = []
vetor_b = []
posicoes_iguais = []

print("A:")
for i in range(5):
    vetor_a.append(int(input()))

print("B:")
for i in range(5):
    vetor_b.append(int(input()))

for i in range(5):
    if vetor_a[i] == vetor_b[i]:
        posicoes_iguais.append(i)

print()
if len(posicoes_iguais) == 0:
    print("NENHUMA POSIÇÃO")
else:
    print("Posições iguais:", end=" ")
    for i in range(len(posicoes_iguais)):
        separador = ", " if i < len(posicoes_iguais) - 1 else ""
        print(posicoes_iguais[i], end=separador)
    print()