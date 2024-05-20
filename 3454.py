jogada = input()

if jogada == "XOX":
    print("*")
elif jogada == "XXO" or jogada == "OXX":
    print("Alice")
else:
    print("?")