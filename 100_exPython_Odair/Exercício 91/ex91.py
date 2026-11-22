def contarPositivos(vetor):
    contador = 0
    for numero in vetor:
        if numero > 0:
            contador += 1
    return contador


# Programa principal
entrada = input("Introduza os números do vetor separados por espaço: ").split()
vetor = [float(x.replace(",", ".")) for x in entrada]

quantidade = contarPositivos(vetor)
print(f"Quantidade de positivos: {quantidade}")

# Verificação com as chamadas de teste
print()
print("Testes da função:")
print(f"contarPositivos([5, -2, 0, 8, -1]) -> {contarPositivos([5, -2, 0, 8, -1])}")
print(f"contarPositivos([1, 2, 3]) -> {contarPositivos([1, 2, 3])}")
print(f"contarPositivos([-1, -2, 0]) -> {contarPositivos([-1, -2, 0])}")