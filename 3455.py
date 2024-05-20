A, B, C = map(int, input().split())

questao_max = input()

if questao_max == "A":
    resultado = int((C* 5/2) + (B * 3/2) + A)
    print(resultado)
elif questao_max == "B":
    resultado = int((C * 5/3) + (A * 2/3) + B)
    print(resultado)
elif questao_max== "C":
        resultado = int((A* 2/5) + (B* 3/5) + C)
        print(resultado)

