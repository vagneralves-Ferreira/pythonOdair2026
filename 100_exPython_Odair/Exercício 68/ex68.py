# Leitura dos 8 números inteiros
vetor = []
for i in range(8):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

# Inicialização com o primeiro elemento (índice 0)
menor_valor = vetor[0]
primeira_posicao = 0

# Percorre o restante do vetor (índices 1 a 7)
for i in range(1, 8):
    # O operador '<' garante que apenas a primeira ocorrência seja mantida em caso de empate
    if vetor[i] < menor_valor:
        menor_valor = vetor[i]
        primeira_posicao = i

# Exibição dos resultados
print(f"\nMenor valor: {menor_valor}")
print(f"Primeira posição: {primeira_posicao}")