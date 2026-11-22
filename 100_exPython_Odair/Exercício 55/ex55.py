primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
quantidade = int(input("Quantidade: "))

print()
print("Sequência:", end=" ")

termo_atual = primeiro
soma = 0

for i in range(quantidade):
    print(termo_atual, end=" ")
    soma += termo_atual
    termo_atual += razao

print()
print(f"Soma: {soma}")