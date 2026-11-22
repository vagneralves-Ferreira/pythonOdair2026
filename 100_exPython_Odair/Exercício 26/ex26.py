salario_atual = float(input("Salário atual: R$ ").replace('.', '').replace(',', '.'))

if salario_atual <= 1500.00:
    percentual = "15%"
    novo_salario = salario_atual * 1.15
elif salario_atual <= 3000.00:
    percentual = "10%"
    novo_salario = salario_atual * 1.10
else:
    percentual = "5%"
    novo_salario = salario_atual * 1.05

print(f"\nSalário atual: R$ {salario_atual:.2f}\nPercentual: {percentual}\nNovo salário: R$ {novo_salario:.2f}".replace('.', ','))

input("\nPressione Enter para sair...")