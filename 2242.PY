risada = input()
risada = "".join([chr for chr in risada if chr in "aeiou"])

risada_inversa = risada[::-1]

if risada == risada_inversa:
    print("S\n")
else:
    print("N\n")
