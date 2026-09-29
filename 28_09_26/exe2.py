import math

1010
def calcular_area_circulo(raio):
    """Calcula a área de um círculo dado o raio."""
    return math.pi * (raio ** 2)

def formatar_resultado(valor):
    """Retorna o valor formatado com 2 casas decimais e unidade."""
    return f"{valor:.2f} m²"


print("--- CALCULADORA DE ÁREA DE CÍRCULO ---")

raio_usuario = float(input("Digite o raio do círculo: "))

if raio_usuario < 0:
    print("Erro: o raio deve ser um valor positivo.")
else:
    area = calcular_area_circulo(raio_usuario)
    print(f"A área do círculo é: {formatar_resultado(area)}")