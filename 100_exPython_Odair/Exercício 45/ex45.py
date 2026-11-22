quantidade = int(input("Quantidade de termos: "))

print()

f0 = 0
f1 = 1

for i in range(quantidade):
    print(f0, end=" ")
    f0, f1 = f1, f0 + f1