notas = []
soma = 0.0

print("Notas:")
for i in range(8):
    nota = float(input().replace(",", "."))
    notas.append(nota)
    soma += nota

media = soma / 8

print()
print(f"Média: {media:.1f}".replace(".", ","))
print("Acima da média:", end="")

acima = 0
for nota in notas:
    if nota > media:
        print(f" {nota:g}".replace(".", ","), end="")
        acima += 1

print()
print(f"Quantidade: {acima}")