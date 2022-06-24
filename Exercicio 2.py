num = input("Digite um número de 0 a 102334155: ")

anterior = 0
proximo = 1
soma = 1

listnum = []

for n in range (0, 41):
    soma = proximo + anterior
    anterior = proximo
    proximo = soma
    
    if str(num) == str(soma):
        listnum.append(soma)

if len(listnum) == 0:
    print("O número informado não pertence a sequência de Fibonacci.")
else:
    print("O número informado pertence a sequência de Fibonacci.")