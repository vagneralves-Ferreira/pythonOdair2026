vetor_a = []
vetor_b = []
vetor_c = []

print("A:")
for i in range(5):
    vetor_a.append(int(input()))

print("B:")
for i in range(5):
    vetor_b.append(int(input()))

for i in range(5):
    vetor_c.append(vetor_a[i])
    vetor_c.append(vetor_b[i])

print()
print("C:", end=" ")
for i in range(len(vetor_c)):
    fim = " " if i < len(vetor_c) - 1 else ""
    print(vetor_c[i], end=fim)
print()