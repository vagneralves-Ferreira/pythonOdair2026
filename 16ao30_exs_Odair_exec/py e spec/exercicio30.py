imovel = float(input("Valor do imóvel: R$ "))
salario = float(input("Valor do salário: R$ ")) 
Prazo = int(input("Prazo de pagamento (em anos): "))
print("")
prestacao = imovel / (Prazo * 12)
print(f"Prestação: R$ {prestacao:.2f}")
Limite = salario * 0.3
print(f"Limite: R$ {Limite:.2f}")
if prestacao > Limite:
    print("Resultado: Empréstimo não concedido.")
else:
    print("Resultado: Empréstimo aprovado\n")

input("Pressione Enter para sair...")
