def soma(a, b):
    return a + b


# Programa principal
num1 = float(input("Primeiro número: ").replace(",", "."))
num2 = float(input("Segundo número: ").replace(",", "."))

resultado = soma(num1, num2)
print(f"Resultado: {resultado:g}".replace(".", ","))

# Verificação com as chamadas de teste
print()
print("Testes da função:")
print(f"soma(8, 5) -> {soma(8, 5):g}".replace(".", ","))
print(f"soma(-3, 7) -> {soma(-3, 7):g}".replace(".", ","))
print(f"soma(2.5, 1.5) -> {soma(2.5, 1.5):g}".replace(".", ","))

# Verificação final: uso do retorno dentro de outra expressão
dobro_da_soma = soma(8, 5) * 2
print(f"Dobro de soma(8, 5): {dobro_da_soma:g}".replace(".", ","))