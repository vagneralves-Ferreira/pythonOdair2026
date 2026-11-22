a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))

if a < b + c and b < a + c and c < a + b and (a == b and b == c and c == a ):
    print("Os valores podem formar um triângulo equilátero.")

elif a < b + c and b < a + c and c < a + b and (a == b or b == c or c == a):
    print("Os valores podem formar um triângulo isósceles.")

elif a < b + c and b < a + c and c < a + b and (a != b and b != c and c != a):
    print("Os valores podem formar um triângulo escaleno.")

else:
    print("Os valores não podem formar um triângulo.")  

input("Pressione Enter para sair...")



