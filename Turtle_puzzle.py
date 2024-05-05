testes = int(input())


while testes > 0 :

    tamanho = int(input())
    soma = 0

    for i in range(0, tamanho, 1):

        numero  = int(input())

        if numero < 0:
            numero = abs(numero)
        
        soma += numero

    print(soma)
    testes -= 1

