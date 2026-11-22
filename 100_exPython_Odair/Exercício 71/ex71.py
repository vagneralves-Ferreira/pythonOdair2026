vetor_a = []
vetor_b = []

print("Vetor A:")
for i in range(10):
    valor = float(input().replace(",", "."))
    vetor_a.append(valor)

for valor in vetor_a:
    if valor > 0:
        vetor_b.append(valor)

print()
print("Vetor B:")
if len(vetor_b) == 0:
    print("VETOR VAZIO")
else:
    for i in range(len(vetor_b)):
        fim = " " if i < len(vetor_b) - 1 else ""
        print(f"{vetor_b[i]:g}".replace(".", ","), end=fim)
    print()