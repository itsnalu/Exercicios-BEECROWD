N = int(input())

for i in range(N):
    sobrenome = input()
    nome = sobrenome.lower()

    count = 0

    for j in nome:
        if (j in ['a', 'e', 'i', 'o', 'u']):
            count = 0
            continue
        else:
            count += 1
            if count == 3:
                break

    
    if count == 3:
        print(f"{sobrenome} nao eh facil")
    else:
        print(f"{sobrenome} eh facil")