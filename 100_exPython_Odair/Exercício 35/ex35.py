idade = int(input('Idade: '))
estudante = input('Estudante: ').strip().upper()

paga_meia = idade < 12 or idade >= 60 or estudante == 'SIM'
valor = 15.00 if paga_meia else 30.00

print(f"\nValor do ingresso: R$ {valor:.2f}".replace('.', ','))

input("\nPressione Enter para sair...")