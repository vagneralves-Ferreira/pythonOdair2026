n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2
if n1 > n2:
    n1, n2 = n2, n1

print(f"Ordem crescente: {n1}, {n2}, {n3}")

input("\nPressione Enter para sair...")
