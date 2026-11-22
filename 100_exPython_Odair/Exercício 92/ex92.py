def mediaVetor(vetor):
    soma = 0.0
    quantidade = 0
    for numero in vetor:
        soma += numero
        quantidade += 1
    return soma / quantidade


# Programa principal
entrada = input("Introduza os números do vetor separados por espaço: ").split()
while len(entrada) == 0:
    entrada = input("O vetor deve ter pelo menos um elemento. Introduza novamente: ").split()

vetor = [float(x.replace(",", ".")) for x in entrada]
resultado = mediaVetor(vetor)
print(f"Média dos elementos: {resultado:g}".replace(".", ","))

# Verificação com as chamadas de teste
print()
print("Testes da função:")
print(f"mediaVetor([2, 4, 6, 8]) -> {mediaVetor([2, 4, 6, 8]):g}".replace(".", ","))
print(f"mediaVetor([10, 10, 10]) -> {mediaVetor([10, 10, 10]):g}".replace(".", ","))
print(f"mediaVetor([-5, 5]) -> {mediaVetor([-5, 5]):g}".replace(".", ","))

# Verificação final: vetor com um único elemento
print(f"mediaVetor([7.5]) -> {mediaVetor([7.5]):g}".replace(".", ","))