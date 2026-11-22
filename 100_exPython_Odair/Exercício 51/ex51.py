primeiro = float(input("Valor 1: "))
maior = primeiro
menor = primeiro

for i in range(2, 11):
    valor = float(input(f"Valor {i}: "))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print()
print(f"Maior: {maior:g}")
print(f"Menor: {menor:g}")