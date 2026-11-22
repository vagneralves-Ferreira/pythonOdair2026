vetor = []

print("Vetor:")
for i in range(10):
    valor = int(input())
    vetor.append(valor)

print()
encontrou_par = False

for i in range(10):
    if vetor[i] % 2 == 0:
        if not encontrou_par:
            print("Pares encontrados:")
            encontrou_par = True
        print(f"{vetor[i]} — posição {i}")

if not encontrou_par:
    print("NENHUM VALOR PAR")