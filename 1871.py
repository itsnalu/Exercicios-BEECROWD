while True:
    N, M = map(int, input().split())
    
    if N == 0 and M == 0:
        break
    soma = N + M
    soma = str(soma)
    nova_soma = "".join([char for char in soma if char != '0'])
    print(nova_soma)