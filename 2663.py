n=int(input())
c=int(input())
lista=[]

for i in range(n):
    lista.append(int(input()))
lista.sort(reverse=True)

indice_ultimo_classificado=c-1
nota_ultimo_classificado= lista[indice_ultimo_classificado]
lista=lista[indice_ultimo_classificado:]
qtd=lista.count(nota_ultimo_classificado)

if(qtd>1):
    qtd-=1
    c+=qtd
    
print(c)