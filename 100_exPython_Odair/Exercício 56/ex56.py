tentativas_invalidas = 0
nota = float(input("Nota: ").replace(",", "."))

while nota < 0 or nota > 10:
    print("Valor inválido.")
    tentativas_invalidas += 1
    nota = float(input("Nota: ").replace(",", "."))

print()
print(f"Nota aceita: {nota:g}".replace(".", ","))
print(f"Tentativas inválidas: {tentativas_invalidas}")