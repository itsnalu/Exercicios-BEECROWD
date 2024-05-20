N = int(input())


for i in range(N):
    texto = input()
    texto = texto.lower()
    texto = texto.replace(" ", "")
    frequencias = {}
    frequencia_max = 0

    for char in texto:
        if char in frequencias:
            frequencias[char] += 1
        else:
            frequencias[char] = 1

        if frequencias[char] > frequencia_max:
            frequencia_max = frequencias[char]
            