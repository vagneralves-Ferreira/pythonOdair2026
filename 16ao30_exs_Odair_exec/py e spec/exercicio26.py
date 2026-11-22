salario  = float(input("Digite o salário atual: R$ "))

if salario <= 1500.00:
    reajuste = salario * 0.15
    print(f"Novo salario R$ {salario + reajuste:.2f}")

elif salario >= 1500.01 and salario <= 3000.00:
    reajuste = salario * 0.10
    print(f"Novo salario R$ {salario + reajuste:.2f}")

elif salario >= 3000.01:
    reajuste = salario * 0.05
    print(f"Novo salario R$ {salario + reajuste:.2f}") 

else:
    print("Salário inválido")

input("Pressione Enter para sair...")
 