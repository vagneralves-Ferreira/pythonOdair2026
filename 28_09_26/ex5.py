import math


def calcular_hipotenusa(cateto_a, cateto_b):
    """Calcula a hipotenusa de um triângulo retângulo pelo Teorema de Pitágoras."""
    hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)
    return hipotenusa


print("--- CÁLCULO DE HIPOTENUSA (TEOREMA DE PITÁGORAS) ---")

cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))

if cateto1 < 0 or cateto2 < 0:
    print("Erro: os catetos devem ser valores positivos.")
else:
    resultado = calcular_hipotenusa(cateto1, cateto2)
    print(f"A hipotenusa é: {resultado:.2f}")