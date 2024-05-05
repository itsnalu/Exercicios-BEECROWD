palavras = int(input())

texto = input()
texto = texto.split()
    
for i in range(palavras):
    if len(texto[i]) == 3 and texto[i][0] == "O" and texto[i][1] == "B":
        texto[i] = "OBI"
    elif len(texto[i]) == 3 and texto[i][0] == "U" and texto[i][1] == "R":
        texto[i] = "URI"

texto = " ".join(texto)

print(texto)
