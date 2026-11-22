primeira = float(input("Altura 1: ").replace(",", "."))
soma = primeira
maior = primeira
menor = primeira

for i in range(2, 9):
    altura = float(input(f"Altura {i}: ").replace(",", "."))
    soma += altura
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura

media = soma / 8

print()
print(f"Média: {media:.2f} m".replace(".", ","))
print(f"Maior: {maior:.2f} m".replace(".", ","))
print(f"Menor: {menor:.2f} m".replace(".", ","))