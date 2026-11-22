a = int(input("A: "))
b = int(input("B: "))

inicio = min(a, b)
fim = max(a, b)
soma = 0

for numero in range(inicio, fim + 1):
    if numero % 3 == 0:
        soma += numero

print()
print(f"Soma dos múltiplos de 3: {soma}")