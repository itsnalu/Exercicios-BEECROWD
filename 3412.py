
N = int(input())

nomes = []
notas = []


for i in range(N):
    nome = input()
    nota = input()
    nomes.append(nome)
    notas.append(nota)


for i in range(len(notas)):    
    nota_split = notas[i].split(" ")
    nota_split = [float(n) for n in nota_split]
    
    if len(nota_split) == 1:
        media = nota_split[0] / 2
        print(f"{nomes[i]}: {media:.1f}")
    elif len(nota_split) == 2:
        media = sum(nota_split) / 2
        print(f"{nomes[i]}: {media:.1f}")
    elif len(nota_split) == 3:
        media = sum(nota_split) / 3
        print(f"{nomes[i]}: {media:.1f}")
    elif len(nota_split) == 4:
        nota_split_sorted = sorted(nota_split, reverse=True)  
        media = sum(nota_split_sorted[:3]) / 3  
        print(f"{nomes[i]}: {media:.1f}")
        
