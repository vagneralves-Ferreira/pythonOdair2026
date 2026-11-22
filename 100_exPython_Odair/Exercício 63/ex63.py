vetor = []

print("Entrada:")
for i in range(8):
    valor = int(input())
    vetor.append(valor)

print()
print("Saída:")
for i in range(7, -1, -1):
    print(vetor[i], end=" ")
print()