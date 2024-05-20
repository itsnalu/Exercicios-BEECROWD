loteria = []

while True:
    string_numero = input()
    
    if string_numero == 'caw caw':
        break

    decimal = 0
    for i in range(3):
        if string_numero[i] == '*':
            decimal += 2 ** (2 - i)

loteria.append(decimal)

for numero in loteria:
    print(numero)
