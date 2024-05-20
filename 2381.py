N, k = map(int, input().split())
chamada = []

for i in range(N):
    nome = input()
    chamada.append(nome)

ordenada = sorted(chamada)

print(ordenada[k-1])
