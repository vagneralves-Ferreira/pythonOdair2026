import math

numero = float(input("Digite um número decimal positivo: "))

if numero < 0:
    print("Erro: o número deve ser positivo.")
else:
    raiz = math.sqrt(numero)

    para_cima = math.ceil(numero)

    para_baixo = math.floor(numero)

    print(f"Raiz quadrada: {raiz:.2f}")
    print(f"Arredondado para cima: {para_cima}")
    print(f"Arredondado para baixo: {para_baixo}")
