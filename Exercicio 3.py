import json

with open("dados.json") as meu_json:
    dados = json.load(meu_json)

fat = 0
maior = 0
menor = 0
soma = 0
media = 0
dias = 0

for i in dados:
    if (i['valor']) != 0:
        fat = i['valor']
        dias += 1
        if (fat > maior):
            maior = fat

        if(menor == 0):
            menor = fat
        elif (fat < menor):
            menor = fat

        soma += i['valor']

print(f'O maior faturamento do mês foi: R$ {maior:.2f}')
print(f'O menor faturamento do mês foi: R$ {menor:.2f}')

media = soma / dias
print(f"A media mensal foi: R$ {media:.2f}")

fatMaiorQueMedia = ''

for n in dados:
    if (n['valor']) != 0:
        # Caso o valor do faturamento do dia for maior que a média, salva o número do dia na String
        if (n['valor']) > media:
           fatMaiorQueMedia += (str(n['dia']) + ' ')
        
print('Os dias em que o faturamento foi maior que a média mensal foram: ' + fatMaiorQueMedia)
        