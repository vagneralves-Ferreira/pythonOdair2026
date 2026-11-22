peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.1f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
  
elif imc >= 18.5 and imc <= 25.0:
    print("Classificação: Peso normal")
   
elif imc >= 25.0 and imc <= 30.0:
   print("Classificação: Acima do peso")
   
elif imc >= 30.0:
    print("Classificação: Obesidade")
    
else:
    print("Classificação: IMC inválido")

input("Pressione Enter para sair...")
