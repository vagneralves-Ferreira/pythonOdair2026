def fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# Programa principal
numero = int(input("Número inteiro (0 a 12): "))
while numero < 0 or numero > 12:
    numero = int(input("Valor inválido. Introduza um inteiro de 0 até 12: "))

print(f"{numero}! = {fatorial(numero)}")

# Verificação com as chamadas de teste
print()
print("Testes da função:")
for valor in [0, 1, 5, 6]:
    print(f"fatorial({valor}) -> {fatorial(valor)}")