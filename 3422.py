N = int(input())

for i in range(N):
    instante, tempo = input().split()

    instante = int(instante)

    if tempo == "1T":
        if instante > 45:
            print(f"45+{instante - 45}")
        else:
            print(instante)
    elif tempo == "2T":
        if instante > 45:
            print(f"90+{instante - 45}")
        else:
            print(instante + 45)

