def totalVendas(vetor):
    total = 0.0
    for valor in vetor:
        total += valor
    return total


def mediaVendas(vetor):
    quantidade = 0
    for _ in vetor:
        quantidade += 1
    return totalVendas(vetor) / quantidade


def maiorVenda(vetor):
    maior = vetor[0]
    for valor in vetor:
        if valor > maior:
            maior = valor
    return maior


def contarAcimaDaMedia(vetor):
    media = mediaVendas(vetor)
    contador = 0
    for valor in vetor:
        if valor > media:
            contador += 1
    return contador


# Validação com o conjunto reduzido de teste
teste_reduzido = [100, 250, 80, 300, 270]
print("Conjunto reduzido para teste:")
print("100 250 80 300 270")
print(f"Total: {totalVendas(teste_reduzido):g}".replace(".", ","))
print(f"Média: {mediaVendas(teste_reduzido):g}".replace(".", ","))
print(f"Maior venda: {maiorVenda(teste_reduzido):g}".replace(".", ","))
print(f"Acima da média: {contarAcimaDaMedia(teste_reduzido)}")
print()

# Programa principal: leitura das dez vendas previstas no enunciado
vendas = []
for i in range(1, 11):
    valor = float(input(f"Valor da {i}ª venda: ").replace(",", "."))
    vendas.append(valor)

print()
print(f"Total: {totalVendas(vendas):g}".replace(".", ","))
print(f"Média: {mediaVendas(vendas):g}".replace(".", ","))
print(f"Maior venda: {maiorVenda(vendas):g}".replace(".", ","))
print(f"Acima da média: {contarAcimaDaMedia(vendas)}")