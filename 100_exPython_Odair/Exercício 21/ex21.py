nota1 = float(input("Primeira nota: ").replace(',', '.'))
nota2 = float(input("Segunda nota: ").replace(',', '.'))

media = (nota1 + nota2) / 2
print(f"Média: {media}")

if media >= 7.0:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")

input("\nPressione Enter para sair...")