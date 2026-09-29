x = 10 # Variável global

def alterar_valor():
    global x  # indica que vamos usar e modificar a variável global
    x = 5
    print(f"Valor dentro da função: {x}")

alterar_valor()
print(f"Valor fora da função: {x}")