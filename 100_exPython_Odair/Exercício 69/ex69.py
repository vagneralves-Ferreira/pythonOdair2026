# Leitura dos 10 números inteiros
vetor = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

# Leitura do valor a ser procurado
valor_procurado = int(input("\nValor procurado: "))

# Lista para armazenar os índices onde o valor aparece
posicoes = []

# Percorre o vetor (índices 0 a 9)
for i in range(10):
    if vetor[i] == valor_procurado:
        posicoes.append(str(i))

# Verificação final e exibição do resultado
if len(posicoes) > 0:
    print(f"Posições: {', '.join(posicoes)}")
else:
    print("VALOR NÃO ENCONTRADO")