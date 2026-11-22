dias = ['SEGUNDA-FEIRA', 'TERÇA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SÁBADO', 'DOMINGO']
numero = int(input('Digite um número de 1 a 7: '))

print(f"Resultado: {dias[numero - 1] if 1 <= numero <= 7 else 'OPÇÃO INVÁLIDA'}")

input("\nPressione Enter para sair...")