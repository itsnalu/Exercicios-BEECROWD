while True:
  try:
    palavra = input()
    tamanho = len(palavra)

    index_ini = tamanho -2
    index_fim = tamanho - 1

    for i in range(tamanho):
        if palavra[index_ini] == palavra[index_fim]:
            break
        else:
            index_ini -= 1

    metade = palavra[:(tamanho//2)]
    outra_metade = palavra[(tamanho//2):]

    if index_ini == -1:
       print(palavra)
    elif outra_metade == metade:
        print(metade)
    else:      
        nova = palavra[0:(index_ini+1)]
        print(nova)
            
  except EOFError:
    break

