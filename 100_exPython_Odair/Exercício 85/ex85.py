def media3(n1, n2, n3):
    return (n1 + n2 + n3) / 3


# Programa principal
nota1 = float(input("Primeira nota: ").replace(",", "."))
nota2 = float(input("Segunda nota: ").replace(",", "."))
nota3 = float(input("Terceira nota: ").replace(",", "."))

resultado = media3(nota1, nota2, nota3)
print(f"Média: {resultado:.2f}".replace(".", ","))

# Verificação com as chamadas de teste
print()
print("Testes da função:")
print(f"media3(8, 7, 6) -> {media3(8, 7, 6):.2f}".replace(".", ","))
print(f"media3(10, 9, 8) -> {media3(10, 9, 8):.2f}".replace(".", ","))
print(f"media3(5.5, 6.5, 7) -> {media3(5.5, 6.5, 7):.2f}".replace(".", ","))

# Verificação final: três notas iguais
print(f"media3(7.5, 7.5, 7.5) -> {media3(7.5, 7.5, 7.5):.2f}".replace(".", ","))