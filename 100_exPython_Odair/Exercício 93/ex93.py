def maiorVetor(vetor):
    maior = vetor[0]
    for elemento in vetor:
        if elemento > maior:
            maior = elemento
    return maior


# Programa principal
entrada = input("Introduza os números do vetor separados por espaço: ").split()
while len(entrada) == 0:
    entrada = input("O vetor não pode estar vazio. Introduza novamente: ").split()

vetor = [float(x.replace(",", ".")) for x in entrada]
resultado = maiorVetor(vetor)
print(f"Maior valor do vetor: {resultado:g}".replace(".", ","))

# Verificação com as chamadas de teste
print()
print("Testes da função:")
print(f"maiorVetor([4, 7, 2, 9, 5]) -> {maiorVetor([4, 7, 2, 9, 5]):g}".replace(".", ","))
print(f"maiorVetor([-8, -2, -5]) -> {maiorVetor([-8, -2, -5]):g}".replace(".", ","))
print(f"maiorVetor([3, 3, 3]) -> {maiorVetor([3, 3, 3]):g}".replace(".", ","))

# Verificação final: vetor contendo apenas números negativos
print(f"maiorVetor([-15, -4, -22, -9]) -> {maiorVetor([-15, -4, -22, -9]):g}".replace(".", ","))