N = int(input())
caminhos = []
pastas = []

for i in range(N):
    caminho = input()
    caminhos.append(caminho)

caminhos.sort()

pasta_referencia = ""
primeiro = caminhos[0]
ultimo = caminhos[-1]

for i in range(min(len(primeiro), len(ultimo))):
    if primeiro[i] == ultimo[i]:
        pasta_referencia += primeiro[i]
    else:
        break



caminhos_modificados = [caminho.replace(pasta_referencia+ "/", "") for caminho in caminhos]


total = sum(len(caminho) for caminho in caminhos_modificados)
print(total)


