ladoA = float(input("Digite o Lado A: ").replace(',', '.'))
ladoB = float(input("Digite o Lado B: ").replace(',','.'))
ladoC = float(input("Digite o Lado C: ").replace(',', '.'))

print(f"\nLados: {ladoA}, {ladoB} e {ladoC}")

if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
    if ladoA == ladoB == ladoC:
        resultado = "EQUILÁTERO"
    elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
        resultado = "ESCALENO"
    else:
        resultado = "ISÓSCELES"
else:
    resultado = "NÃO FORMA TRIÂNGULO"

print(f"Resultado: {resultado}")

input("\nPressione Enter para sair")


