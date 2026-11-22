soma = 0.0

for i in range(5):
    valor = float(input(f"Valor {i + 1}: "))
    soma += valor

print()
print(f"Soma: {soma:g}")