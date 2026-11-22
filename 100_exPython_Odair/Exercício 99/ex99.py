def formatarMoeda(valor):
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


def valorTotalEstoque(quantidades, precos):
    total = 0.0
    for i in range(len(quantidades)):
        total += quantidades[i] * precos[i]
    return total


def contarEstoqueBaixo(quantidades):
    contador = 0
    for qtd in quantidades:
        if qtd < 5:
            contador += 1
    return contador


def produtoMaiorValorEstoque(nomes, quantidades, precos):
    indice_maior = 0
    maior_valor = quantidades[0] * precos[0]
    for i in range(1, len(nomes)):
        valor_atual = quantidades[i] * precos[i]
        if valor_atual > maior_valor:
            maior_valor = valor_atual
            indice_maior = i
    return nomes[indice_maior], maior_valor


# Validação com o exemplo de execução do enunciado
nomes_teste = ["Teclado", "Mouse", "Cabo", "Headset"]
qtds_teste = [3, 10, 2, 5]
precos_teste = [120.00, 50.00, 20.00, 200.00]

nome_top, valor_top = produtoMaiorValorEstoque(nomes_teste, qtds_teste, precos_teste)
print("Exemplo de execução:")
print(f"Valor total do estoque: {formatarMoeda(valorTotalEstoque(qtds_teste, precos_teste))}")
print(f"Produtos com estoque menor que 5: {contarEstoqueBaixo(qtds_teste)}")
print(f"Maior valor em estoque: {nome_top} — {formatarMoeda(valor_top)}")
print()

# Programa principal: leitura de oito produtos
nomes = []
quantidades = []
precos = []

for i in range(1, 9):
    nome = input(f"Nome do {i}º produto: ").strip()
    qtd = int(input(f"Quantidade de {nome}: "))
    preco = float(input(f"Preço unitário de {nome} (R$): ").replace(",", "."))
    nomes.append(nome)
    quantidades.append(qtd)
    precos.append(preco)

total_estoque = valorTotalEstoque(quantidades, precos)
estoque_baixo = contarEstoqueBaixo(quantidades)
nome_maior, valor_maior = produtoMaiorValorEstoque(nomes, quantidades, precos)

print()
print(f"Valor total do estoque: {formatarMoeda(total_estoque)}")
print(f"Produtos com estoque menor que 5: {estoque_baixo}")
print(f"Maior valor em estoque: {nome_maior} — {formatarMoeda(valor_maior)}")