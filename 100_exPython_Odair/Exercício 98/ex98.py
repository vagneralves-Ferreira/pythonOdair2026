def mediaTemperaturas(temperaturas):
    soma = 0.0
    quantidade = 0
    for temp in temperaturas:
        soma += temp
        quantidade += 1
    return soma / quantidade


def maiorTemperatura(temperaturas):
    maior = temperaturas[0]
    for temp in temperaturas:
        if temp > maior:
            maior = temp
    return maior


def menorTemperatura(temperaturas):
    menor = temperaturas[0]
    for temp in temperaturas:
        if temp < menor:
            menor = temp
    return menor


def diasAcimaDaMedia(temperaturas):
    media = mediaTemperaturas(temperaturas)
    contador = 0
    for temp in temperaturas:
        if temp > media:
            contador += 1
    return contador


# Validação com o exemplo de execução do enunciado
exemplo = [22, 25, 19, 28, 24, 26, 20]
print("Exemplo de execução:")
print("Temperaturas:")
print("22 25 19 28 24 26 20")
print()
print(f"Média: {mediaTemperaturas(exemplo):.2f}".replace(".", ","))
print(f"Maior: {maiorTemperatura(exemplo):g}".replace(".", ","))
print(f"Menor: {menorTemperatura(exemplo):g}".replace(".", ","))
print(f"Dias acima da média: {diasAcimaDaMedia(exemplo)}")
print()

# Programa principal: leitura de exatamente sete temperaturas
dias_semana = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
]
temperaturas = []

for dia in dias_semana:
    valor = float(input(f"Temperatura de {dia}: ").replace(",", "."))
    temperaturas.append(valor)

print()
print(f"Média: {mediaTemperaturas(temperaturas):.2f}".replace(".", ","))
print(f"Maior: {maiorTemperatura(temperaturas):g}".replace(".", ","))
print(f"Menor: {menorTemperatura(temperaturas):g}".replace(".", ","))
print(f"Dias acima da média: {diasAcimaDaMedia(temperaturas)}")