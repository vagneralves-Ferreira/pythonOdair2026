nomes = []
notas = []
soma = 0.0

for i in range(5):
    nome = input(f"Nome {i + 1}: ")
    nota = float(input(f"Nota {i + 1}: ").replace(",", "."))
    nomes.append(nome)
    notas.append(nota)
    soma += nota

media = soma / 5
acima_media = []

for i in range(5):
    if notas[i] > media:
        acima_media.append(nomes[i])

print()
print(f"Média: {media:.1f}".replace(".", ","))
print("Acima da média:", end=" ")
for i in range(len(acima_media)):
    separador = ", " if i < len(acima_media) - 1 else ""
    print(acima_media[i], end=separador)
print()