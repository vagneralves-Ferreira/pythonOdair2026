def calcularMedia(notas):
    soma = 0.0
    quantidade = 0
    for nota in notas:
        soma += nota
        quantidade += 1
    return soma / quantidade


def maiorNota(notas):
    maior = notas[0]
    for nota in notas:
        if nota > maior:
            maior = nota
    return maior


def menorNota(notas):
    menor = notas[0]
    for nota in notas:
        if nota < menor:
            menor = nota
    return menor


def alunosAcimaDaMedia(nomes, notas):
    media = calcularMedia(notas)
    acima = []
    for i in range(len(notas)):
        if notas[i] > media:
            acima.append(nomes[i])
    return acima


# Validação com o exemplo de execução do enunciado
nomes_teste = ["Ana", "Bruno", "Carla", "Diego", "Eva"]
notas_teste = [8, 6, 9, 7, 5]

print("Exemplo de execução:")
print(f"Média: {calcularMedia(notas_teste):g}".replace(".", ","))
print(f"Maior nota: {maiorNota(notas_teste):g}".replace(".", ","))
print(f"Menor nota: {menorNota(notas_teste):g}".replace(".", ","))
print(f"Acima da média: {', '.join(alunosAcimaDaMedia(nomes_teste, notas_teste))}")
print()

# Programa principal: leitura de 8 alunos com vetores paralelos
nomes = []
notas = []

for i in range(1, 9):
    nome = input(f"Nome do {i}º aluno: ").strip()
    nota = float(input(f"Nota de {nome}: ").replace(",", "."))
    nomes.append(nome)
    notas.append(nota)

media_turma = calcularMedia(notas)
maior = maiorNota(notas)
menor = menorNota(notas)
lista_acima = alunosAcimaDaMedia(nomes, notas)

print()
print(f"Média: {media_turma:g}".replace(".", ","))
print(f"Maior nota: {maior:g}".replace(".", ","))
print(f"Menor nota: {menor:g}".replace(".", ","))
print(f"Acima da média: {', '.join(lista_acima) if lista_acima else 'Nenhum'}")