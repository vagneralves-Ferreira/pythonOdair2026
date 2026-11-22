numero = float(input("Digite um número: ").replace(',', '.'))

if numero > 0:
    print("Resultado: POSITIVO")
elif numero < 0:
    print("Resultado: NEGATIVO")
else:
    print("Resultado: ZERO")

input("\nPressione Enter para sair...")