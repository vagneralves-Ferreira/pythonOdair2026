ano = int(input("Ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("\nResultado: ANO BISSEXTO")
else:
    print("\nResultado: NÃO BISSEXTO")

input("\nPressione Enter para sair...")
