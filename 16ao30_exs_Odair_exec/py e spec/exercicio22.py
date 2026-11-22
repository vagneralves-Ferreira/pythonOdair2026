nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) /2
print(f"Média:{media: .2f}")

if media< 5.0:
    print("REPROVADO")

elif media >= 5.0 and media < 7.0:
    print("RECUPERAÇÃO")

else:
    print("APROVADO")

input("Pressione ENTER para sair...")