senha_correta = "1234"
tentativas = 0

while True:
    senha = input("Senha: ")
    tentativas += 1
    if senha == senha_correta:
        break
    print("Senha incorreta.")

print()
print("ACESSO LIBERADO")
print(f"Tentativas: {tentativas}")