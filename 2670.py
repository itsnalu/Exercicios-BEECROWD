primeiro = int(input())
segundo = int(input())
terceiro = int(input())

caminho1 = (segundo * 2) + (terceiro * 4)
caminho2 = (primeiro * 2) + (terceiro * 2)
caminho3 = (primeiro * 4) + (segundo * 2)

lista=[caminho1, caminho2, caminho3]

lista.sort()

print(lista[0])