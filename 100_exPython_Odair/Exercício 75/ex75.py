vetor = []

print("Entrada:")
for i in range(10):
    vetor.append(int(input()))

n = len(vetor)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if vetor[j] > vetor[j + 1]:
            vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

print()
print("Saída:")
for i in range(n):
    fim = " " if i < n - 1 else ""
    print(vetor[i], end=fim)
print()