N = int(input())
pessoas = input().split()

for i in range(N):
    pessoas[i] = int(pessoas[i])

menor = min(pessoas)
numero = pessoas.index(menor) + 1

print(numero)