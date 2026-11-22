# Leitura dos 10 números inteiros
vetor = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

# Leitura do valor de busca
valor_procurado = int(input("\nValor procurado: "))

# Contador de ocorrências inicializado a zero
ocorrencias = 0

# Percorre o vetor e incrementa o contador sempre que encontra o valor
for numero in vetor:
    if numero == valor_procurado:
        ocorrencias += 1

# Exibição do resultado
print(f"Ocorrências: {ocorrencias}")