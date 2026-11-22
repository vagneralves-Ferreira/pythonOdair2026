peso = float(input("Digite o peso: ").lower().replace('kg', '').replace(',', '.').strip())
altura = float(input("Digite a altura: ").lower().replace('m', '').replace(',', '.').strip())

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25.0: 
    classificacao = "FAIXA NORMAL"
elif imc < 30.0:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"

print(f"\nIMC: {imc:.1f}".replace('.', ','))
print(f"Classificação: {classificacao}")

input("\nPressione enter para sair...")