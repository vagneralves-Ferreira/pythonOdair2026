def contarOcorrencias(vetor, alvo):
    contador = 0
    for elemento in vetor:
        if elemento == alvo:
            contador += 1
    return contador


# Programa principal
entrada = input("Introduza os números do vetor separados por espaço: ").split()
vetor = [float(x.replace(",", ".")) for x in entrada]
valor_procurado = float(input("Valor a procurar: ").replace(",", "."))

quantidade = contarOcorrencias(vetor, valor_procurado)
print(f"Quantidade de ocorrências: {quantidade}")

# Verificação com as chamadas de teste
print()
print("Testes da função:")
print(f"contarOcorrencias([3, 5, 3, 8, 3], 3) -> {contarOcorrencias([3, 5, 3, 8, 3], 3)}")
print(f"contarOcorrencias([1, 2, 3], 4) -> {contarOcorrencias([1, 2, 3], 4)}")
print(f"contarOcorrencias([7, 7, 7, 7], 7) -> {contarOcorrencias([7, 7, 7, 7], 7)}")