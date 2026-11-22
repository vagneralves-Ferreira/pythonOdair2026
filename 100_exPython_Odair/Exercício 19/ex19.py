num1 = float(input("Primeiro número: ").replace(',', '.'))
num2 = float(input("Segundo número: ").replace(',', '.'))
num3 = float(input("Terceiro número: ").replace(',', '.'))

Maior = num1
Menor = num1

if num2 > Maior:
    Maior = num2
if num2 < Menor:
    Menor = num2

if num3 > Maior:
    Maior = num3
if num3 < Menor:
    Menor = num3

print(f"\nMaior: {Maior:g}")
print(f"Menor: {Menor:g}")

input("\nPressione Enter para sair...")
      