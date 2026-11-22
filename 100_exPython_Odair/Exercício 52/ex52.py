soma_idades = 0
menores_18 = 0
idosos_60_mais = 0

for i in range(10):
    idade = int(input(f"Idade {i + 1}: "))
    soma_idades += idade
    
    if idade < 18:
        menores_18 += 1
    elif idade >= 60:
        idosos_60_mais += 1

media = soma_idades / 10

print()
print(f"Média: {media:g}".replace(".", ","))
print(f"Menores de 18: {menores_18}")
print(f"Com 60 anos ou mais: {idosos_60_mais}")