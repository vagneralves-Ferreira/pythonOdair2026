numero = int(input("Número: "))
inicio = int(input("Início: "))
fim = int(input("Fim: "))

print()

if inicio <= fim:
    for i in range(inicio, fim + 1):
        print(f"{numero} x {i} = {numero * i}")
else:
    for i in range(inicio, fim - 1, -1):
        print(f"{numero} x {i} = {numero * i}")