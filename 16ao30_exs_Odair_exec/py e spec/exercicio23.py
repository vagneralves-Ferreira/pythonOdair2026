idade = int(input("Idade: "))

if idade < 16:
    print("Não pode votar")

elif idade == 16 or idade == 17:
    print("Voto opicional")

elif idade == 18 or idade <= 69:
    print("Voto obrigatório")

else:
    print("Voto opicional")

input("Pressione ENTER para sair...")
