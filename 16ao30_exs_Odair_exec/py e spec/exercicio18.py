n1 = int(input("Primeiro valor : "))
n2 = int(input("Segundo valor : "))

if n1 > n2:
    print(f"O maior valor é {n1}")  
elif n2 > n1:
    print(f"O maior valor é {n2}")  
else:
    print("Os valores são iguais.")

input("Pressione Enter para sair...")
