while True:
    try:
        word=input()
        tamanho=len(word)
        
        for i in range(tamanho):
            print(" "*i,end='')
            c=0;
            for j in range(0,tamanho-i):
                    print(word[c],end='')
                    c+=1
                    if(j!=tamanho-i-1):
                        print(" ",end='')
                
            print()
    except EOFError:
        break