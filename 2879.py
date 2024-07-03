n = int(input())
vetor = []
vitoria = 0

for i in range(n):
    vetor.append(int(input()))
    if vetor[i] != 1:
        vitoria += 1

print(vitoria)

