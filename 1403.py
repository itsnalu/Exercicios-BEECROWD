vetorzin=[]
while True:
    result=''
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    matriz = []

    for i in range(n):
        vetor = list(map(int, input().split()))
        matriz.append(vetor)

    valores_unicos = set()
    for linha in matriz:
        for valor in linha:
            valores_unicos.add(valor)

    frequencia = {}
    for linha in matriz:
        for valor in linha:
            if valor in frequencia:
                frequencia[valor] += 1
            else:
                frequencia[valor] = 1

    frequencias_ordenadas = sorted(frequencia.values(), reverse=True)
    if(len(frequencias_ordenadas)>1):
        segundo_maior = frequencias_ordenadas[1]
    else: segundo_maior = frequencias_ordenadas[0]
    
    valores_segunda_maior = [valor for valor, freq in frequencia.items() if freq == segundo_maior]
    
    
    valores_segunda_maior.sort()
    result = ' '.join(map(str, valores_segunda_maior))
    result+=" "
    print(result)