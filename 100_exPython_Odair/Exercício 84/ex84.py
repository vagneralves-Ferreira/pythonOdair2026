def ehPar(numero):
    return numero % 2 == 0


# Programa principal
valor = int(input("Número inteiro: "))
resultado = "verdadeiro" if ehPar(valor) else "falso"
print(f"Resultado: {resultado}")

# Verificação com as chamadas de teste
print()
print("Testes da função:")
for n in [8, 13, 0, -4]:
    saida = "verdadeiro" if ehPar(n) else "falso"
    print(f"ehPar({n}) -> {saida}")