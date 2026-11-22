def celsiusParaFahrenheit(celsius):
    return celsius * 9 / 5 + 32


# Programa principal
temp_c = float(input("Temperatura em Celsius: ").replace(",", "."))
temp_f = celsiusParaFahrenheit(temp_c)
print(f"Temperatura em Fahrenheit: {temp_f:g}".replace(".", ","))

# Verificação com as chamadas de teste
print()
print("Testes da função:")
print(f"celsiusParaFahrenheit(0) -> {celsiusParaFahrenheit(0):g}".replace(".", ","))
print(f"celsiusParaFahrenheit(25) -> {celsiusParaFahrenheit(25):g}".replace(".", ","))
print(f"celsiusParaFahrenheit(-40) -> {celsiusParaFahrenheit(-40):g}".replace(".", ","))