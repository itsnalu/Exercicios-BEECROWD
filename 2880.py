mensagem = input()
crib = input()

pos = 0
tam_m = len(mensagem)
tam_c = len(crib)

posicoes = (tam_m - tam_c) + 1
count = posicoes
print(count)

for j in range(posicoes):
    comparar = mensagem[j::count]
    comparado = crib

    print(comparar)


    for i in range(tam_c):
        if comparado[i] == comparar[i]:
            break
        elif i == (tam_c-2):
            pos += 1
        
    count += 1

print(pos)