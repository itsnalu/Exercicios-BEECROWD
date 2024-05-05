n = int(input())

for caso in range(1, n+1):
    valor, formato = input().split()

    if formato == 'bin':
        valor = int(valor, 2) 
        print(f'Case {caso}:')
        print(f'{valor} dec')   
        print(f'{hex(valor)[2:]} hex\n')
    
    elif formato == 'dec':      
        valor = int(valor)
        print(f'Case {caso}:')    
        print(f'{hex(valor)[2:]} hex')
        print(f'{bin(valor)[2:]} bin\n')


    elif formato == 'hex':
        valor = int(valor, 16)
        print(f'Case {caso}:')
        print(f'{valor} dec')   
        print(f'{bin(valor)[2:]} bin\n')



