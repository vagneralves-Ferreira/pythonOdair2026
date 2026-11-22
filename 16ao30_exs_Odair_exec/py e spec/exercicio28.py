l1 = int(input("Digite o valor do lado 1: "))
l2 = int(input("Digite o valor do lado 2: "))
l3 = int(input("Digite o valor do lado 3: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os valores podem formar um triângulo.")
else:
    print("Os valores não podem formar um triângulo.")

input("Pressione Enter para sair...")
