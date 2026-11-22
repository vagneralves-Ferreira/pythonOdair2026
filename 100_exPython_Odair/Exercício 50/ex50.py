maior = float(input("Valor 1: "))

for i in range(2, 11):
    valor = float(input(f"Valor {i}: "))
    if valor > maior:
        maior = valor

print()
print(f"Maior valor: {maior:g}")