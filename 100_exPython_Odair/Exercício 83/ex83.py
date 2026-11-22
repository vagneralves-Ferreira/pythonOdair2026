def menor3(a, b, c):
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor


# Programa principal
num1 = float(input("Primeiro número: ").replace(",", "."))
num2 = float(input("Segundo número: ").replace(",", "."))
num3 = float(input("Terceiro número: ").replace(",", "."))

resultado = menor3(num1, num2, num3)
print(f"Menor valor: {resultado:g}".replace(".", ","))

# Verificação com as chamadas de teste
print()
print("Testes da função:")
print(f"menor3(8, 3, 5) -> {menor3(8, 3, 5):g}".replace(".", ","))
print(f"menor3(-1, -7, -2) -> {menor3(-1, -7, -2):g}".replace(".", ","))
print(f"menor3(4, 4, 9) -> {menor3(4, 4, 9):g}".replace(".", ","))

# Verificação final: menor valor em posições diferentes e com repetição
print(f"menor3(2, 5, 8) -> {menor3(2, 5, 8):g}".replace(".", ","))
print(f"menor3(8, 5, 2) -> {menor3(8, 5, 2):g}".replace(".", ","))
print(f"menor3(9, 4, 4) -> {menor3(9, 4, 4):g}".replace(".", ","))