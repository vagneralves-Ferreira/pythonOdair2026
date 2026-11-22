n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 <= n2 <= n3:
    print(f"Ordem crescente: {n1}, {n2}, {n3}")
elif n1 <= n3 <= n2:
    print(f"Ordem crescente: {n1}, {n3}, {n2}")
elif n2 <= n1 <= n3:
    print(f"Ordem crescente: {n2}, {n1}, {n3}")
elif n2 <= n3 <= n1:
    print(f"Ordem crescente: {n2}, {n3}, {n1}")
elif n3 <= n1 <= n2:
    print(f"Ordem crescente: {n3}, {n1}, {n2}")
else:
    print(f"Ordem crescente: {n3}, {n2}, {n1}")

input("Pressione Enter para sair...")