ladoA = float(input("Digite o Lado A: ").replace(',', '.'))
ladoB = float(input("Digite o Lado B: ").replace(',','.'))
ladoC = float(input("Digite o Lado C: ").replace(',', '.'))

print(f"\nLados: {ladoA}, {ladoB} e {ladoC}")

if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
    resultado = "FORMAM UM TRIÂNGULO"
else:
    resultado = "NÃO FORMAM"

print(f"Resultado: {resultado}")

input("\nPressione Enter para sair...")

