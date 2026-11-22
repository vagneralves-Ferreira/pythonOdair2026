SalarioFixo = float(input("Salário fixo: R$"))
TotalVendido = float(input("Total vendido: R$"))
Comissao = TotalVendido * 0.04
SalarioTotal = SalarioFixo + Comissao

print(f"Comissão: R${Comissao:.2f}")
print(f"Salário total: R${SalarioTotal:.2f}")