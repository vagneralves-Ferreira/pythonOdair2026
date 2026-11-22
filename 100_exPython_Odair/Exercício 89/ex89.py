def notaValida(nota):
    return 0 <= nota <= 10


# Programa principal
valor = float(input("Introduza uma nota: ").replace(",", "."))
resultado = "verdadeiro" if notaValida(valor) else "falso"
print(f"Nota válida: {resultado}")

# Verificação com as chamadas de teste
print()
print("Testes da função:")
for n in [7.5, 0, 10, -1, 10.1]:
    saida = "verdadeiro" if notaValida(n) else "falso"
    print(f"notaValida({f'{n:g}'.replace('.', ',')}) -> {saida}")