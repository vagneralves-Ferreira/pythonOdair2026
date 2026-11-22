numero = int(input("Número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print()
print(f"{numero}! = {fatorial}")