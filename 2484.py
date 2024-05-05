while True:
    try:
        palavra = input()
        espacos = 0
        for i in range(len(palavra), 0, -1):
            linha = " " * espacos + " ".join(palavra[:i])
            print(linha)
            espacos += 1
        print()
    except EOFError:
        break