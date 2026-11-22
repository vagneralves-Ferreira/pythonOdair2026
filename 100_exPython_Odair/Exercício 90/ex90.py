def mostrarTabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


# Programa principal
valor = int(input("Número inteiro: "))
mostrarTabuada(valor)

# Verificação com a chamada de teste
print()
print("Teste do procedimento (mostrarTabuada(4)):")
mostrarTabuada(4)