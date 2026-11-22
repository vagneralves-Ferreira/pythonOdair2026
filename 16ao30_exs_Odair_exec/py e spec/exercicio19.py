n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))        
n3 = int(input("Digite o terceiro número: "))

Maior = n1
if n2 > Maior:
    Maior = n2
if n3 > Maior:
    Maior = n3

Menor = n1
if n2 < Menor:
    Menor = n2
if n3 < Menor:
    Menor = n3

print (f"Valores {n1}, {n2}, {n3}")

print(f"Maior {Maior}")
print(f"Menor {Menor}")

input ("Pressione Enter para sair...")
