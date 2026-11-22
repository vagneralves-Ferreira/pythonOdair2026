nota1 = float(input("Primeira nota: ").replace(',', '.'))
nota2 = float(input("Segunda nota: ").replace(',', '.'))

media = (nota1 + nota2) / 2
print(f"\nMédia: {media:.1f}")

if media < 5.0:
    print("Situação: REPROVADO")
elif media >= 5.0 and media < 7.0:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: APROVADO")

input("\nPressione enter para sair...")

