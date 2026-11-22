pares = 0
impares = 0

for i in range(6):
    valor = int(input(f"Valor {i + 1}: "))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print()
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")