X = int(input())
print(X)
while X >= 10:
    unidade = X % 10
    X = X // 10
    X = X * 3 + unidade
    print(f"{X}")