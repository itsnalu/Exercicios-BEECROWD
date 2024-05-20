while True:
    try:
        entrada = input()
        entrada_inv = entrada.strrcv()

        if entrada == entrada_inv:
            print("0")


    except EOFError:
        break