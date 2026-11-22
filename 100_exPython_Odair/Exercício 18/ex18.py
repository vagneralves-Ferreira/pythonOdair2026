valor1 = float(input("Primeiro valor: ").replace(',', '.'))
valor2 = float(input("Segundo valor: ").replace(',', '.'))

if valor1 > valor2:
    print(f"Maior valor: {valor1}")
elif valor2 > valor1:
    print(f"Maior valor: {valor2}")
else:
    print("VALORES IGUAIS")

input("\nDigite Enter para sair...")