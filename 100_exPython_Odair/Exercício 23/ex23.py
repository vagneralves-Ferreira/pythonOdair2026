idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Categoria: NÃO PODE VOTAR")
elif (idade == 16 or idade == 17) or idade >= 70:
    print("Categoria: VOTO OPCIONAL")
else:
    print("Categoria: VOTO OBRIGATÓRIO")

input("\nPressione Enter para sair...")