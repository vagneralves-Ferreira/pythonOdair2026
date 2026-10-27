# 5. Iterando sobre tuplas
print("5. ITERANDO SOBRE TUPLAS:\n")

cores = ("vermelho", "verde", "azul")
print("Com for simples:")
for cor in cores:
    print(f"  - {cor}")

print("\nCom enumerate:")
for i, cor in enumerate(cores):
    print(f"  {i}: {cor}")

print()

print("="*60 + "\n")

