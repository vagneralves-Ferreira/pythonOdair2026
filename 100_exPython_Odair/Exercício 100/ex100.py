def mediaNotas(notas):
    soma = 0.0
    quantidade = 0
    for nota in notas:
        soma += nota
        quantidade += 1
    return soma / quantidade


def maiorNota(nomes, notas):
    indice_maior = 0
    for i in range(1, len(notas)):
        if notas[i] > notas[indice_maior]:
            indice_maior = i
    return nomes[indice_maior], notas[indice_maior]


def menorNota(nomes, notas):
    indice_menor = 0
    for i in range(1, len(notas)):
        if notas[i] < notas[indice_menor]:
            indice_menor = i
    return nomes[indice_menor], notas[indice_menor]


def contarAprovados(notas):
    aprovados = 0
    for nota in notas:
        if nota >= 7:
            aprovados += 1
    return aprovados


def alunoMaisVelho(nomes, idades):
    indice_mais_velho = 0
    for i in range(1, len(idades)):
        if idades[i] > idades[indice_mais_velho]:
            indice_mais_velho = i
    return nomes[indice_mais_velho], idades[indice_mais_velho]


def alunosAcimaDaMedia(nomes, notas):
    media = mediaNotas(notas)
    acima = []
    for i in range(len(notas)):
        if notas[i] > media:
            acima.append(nomes[i])
    return acima


# Validação com o conjunto reduzido de teste do enunciado
nomes_teste = ["Ana", "Bruno", "Carla", "Diego", "Eva"]
idades_teste = [19, 22, 18, 25, 20]
notas_teste = [8, 6, 9, 7, 5]

nome_max, nota_max = maiorNota(nomes_teste, notas_teste)
nome_min, nota_min = menorNota(nomes_teste, notas_teste)
nome_velho, idade_velho = alunoMaisVelho(nomes_teste, idades_teste)

print("Conjunto reduzido para teste:")
print(f"Média: {mediaNotas(notas_teste):g}".replace(".", ","))
print(f"Maior nota: {nome_max} - {nota_max:g}".replace(".", ","))
print(f"Menor nota: {nome_min} - {nota_min:g}".replace(".", ","))
print(f"Aprovados: {contarAprovados(notas_teste)}")
print(f"Mais velho: {nome_velho} - {idade_velho} anos")
print(f"Acima da média: {', '.join(alunosAcimaDaMedia(nomes_teste, notas_teste))}")
print()

# Programa principal: leitura de dez alunos usando vetores paralelos
nomes = []
idades = []
notas = []

for i in range(1, 11):
    nome = input(f"Nome do {i}º aluno: ").strip()
    idade = int(input(f"Idade de {nome}: "))
    nota = float(input(f"Nota de {nome}: ").replace(",", "."))
    nomes.append(nome)
    idades.append(idade)
    notas.append(nota)

media_turma = mediaNotas(notas)
nome_maior, valor_maior = maiorNota(nomes, notas)
nome_menor, valor_menor = menorNota(nomes, notas)
total_aprovados = contarAprovados(notas)
nome_mais_velho, idade_mais_velho = alunoMaisVelho(nomes, idades)
lista_acima = alunosAcimaDaMedia(nomes, notas)

print()
print(f"Média: {media_turma:g}".replace(".", ","))
print(f"Maior nota: {nome_maior} - {valor_maior:g}".replace(".", ","))
print(f"Menor nota: {nome_menor} - {valor_menor:g}".replace(".", ","))
print(f"Aprovados: {total_aprovados}")
print(f"Mais velho: {nome_mais_velho} - {idade_mais_velho} anos")
print(f"Acima da média: {', '.join(lista_acima) if lista_acima else 'Nenhum'}")