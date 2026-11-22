positivos = 0
negativos = 0
zeros = 0

for i in range(8):
    valor = int(input(f"Valor {i + 1}: "))
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    else:
        zeros += 1

print()
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")