mes = int(input('Mês: '))
ano = int(input('Ano: '))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    dias = '31 dias'
elif mes in [4, 6, 9, 11]:
    dias = '30 dias'
elif mes == 2:
    e_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    dias = '29 dias' if e_bissexto else '28 dias'
else:
    dias = 'MÊS INVÁLIDO'

print(f"Resultado: {dias}")

input("\nPressione Enter para sair...")