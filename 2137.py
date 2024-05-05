while True:
    try:
        teste = int(input())
        codigos = []

        for i in range(teste):
            codigo = input()
            codigos.append(codigo)

        codigos_ord = sorted(codigos)

        
        for codigo in codigos_ord:
            print(codigo)
    except EOFError:
        break