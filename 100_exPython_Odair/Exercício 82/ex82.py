def maior(a, b):
    if a >= b:
        return a
    return b


# Programa principal
num1 = float(input("Primeiro número: ").replace(",", "."))
num2 = float(input("Segundo número: ").replace(",", "."))

resultado = maior(num1, num2)
print(f"Maior valor: {resultado:g}".replace(".", ","))

# Verificação com as chamadas de teste
print()
print("Testes da função:")
print(f"maior(8, 3) -> {maior(8, 3):g}".replace(".", ","))
print(f"maior(4, 11) -> {maior(4, 11):g}".replace(".", ","))
print(f"maior(-2, -7) -> {maior(-2, -7):g}".replace(".", ","))
print(f"maior(5, 5) -> {maior(5, 5):g}".replace(".", ","))