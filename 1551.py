teste = int(input())

for i in range(teste):
    frase = input()
    frase = frase.replace(",", "")
    frase = frase.replace(" ", "")
    unicos = set(frase)
    numero_letras = len(unicos)
    
    if numero_letras == 26:
        print("frase completa")
    elif numero_letras >= 13:
        print("frase quase completa")
    else: 
        print("frase mal elaborada")

