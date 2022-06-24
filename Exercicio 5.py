palavra = input("Digite uma palavra: ")
caracteres = []
inverso = ''

for letra in palavra:
    caracteres.append(letra)

tamanho = len(caracteres) - 1

while tamanho >= 0:
    inverso += (caracteres[tamanho])
    tamanho -= 1

print(inverso)