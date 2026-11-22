def buscarPosicoes(vetor, alvo):
    posicoes = []
    for i in range(len(vetor)):
        if vetor[i] == alvo:
            posicoes.append(i)
    return posicoes


# Programa principal
entrada = input("Introduza os números do vetor separados por espaço: ").split()
vetor = [float(x.replace(",", ".")) for x in entrada]
valor_procurado = float(input("Valor a procurar: ").replace(",", "."))

resultado = buscarPosicoes(vetor, valor_procurado)
print(f"Posições encontradas: {resultado}")

# Verificação com as chamadas de teste
print()
print("Testes da função:")
print(f"buscarPosicoes([4, 7, 2, 7, 9], 7) -> {buscarPosicoes([4, 7, 2, 7, 9], 7)}")
print(f"buscarPosicoes([5, 5, 5], 5) -> {buscarPosicoes([5, 5, 5], 5)}")
print(f"buscarPosicoes([1, 3, 5], 2) -> {buscarPosicoes([1, 3, 5], 2)}")