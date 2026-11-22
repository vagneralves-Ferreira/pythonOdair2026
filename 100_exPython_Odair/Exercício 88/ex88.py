def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    anterior = 0
    atual = 1
    for _ in range(2, n + 1):
        proximo = anterior + atual
        anterior = atual
        atual = proximo

    return atual


# Programa principal
indice = int(input("Índice N (inteiro não negativo): "))
while indice < 0:
    indice = int(input("Valor inválido. Introduza um índice N >= 0: "))

print(f"F({indice}) = {fibonacci(indice)}")

# Verificação com as chamadas de teste
print()
print("Testes da função:")
for valor in [0, 1, 6, 10]:
    print(f"fibonacci({valor}) -> {fibonacci(valor)}")