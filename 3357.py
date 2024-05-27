N, L, Q = map(float,input().split())

nomes = input().split(" ")

tamanho = N
indice = 0

while(L > Q):
    L -= Q
    indice += 1
    if indice == tamanho:
        indice = 0

print("{} {:.1f}".format(nomes[indice], L))
