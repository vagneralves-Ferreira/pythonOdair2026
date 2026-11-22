quantidade = 0
soma = 0
maiores_idade = 0

while True:
    idade = int(input("Idade: "))
    if idade < 0:
        break
    quantidade += 1
    soma += idade
    if idade >= 18:
        maiores_idade += 1

print()

if quantidade == 0:
    print("NENHUMA IDADE INFORMADA")
else:
    media = soma / quantidade
    print(f"Quantidade: {quantidade}")
    print(f"Média: {media:g}".replace(".", ","))
    print(f"Maiores de idade: {maiores_idade}")