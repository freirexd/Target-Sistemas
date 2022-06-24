"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

import json
import pandas as pd

with open("dados.json") as meu_json:
    dados = json.load(meu_json)

df = pd.read_json("dados.json")

valorMax = df['valor'].max()
valorMin = df['valor'].min()
media = df['valor'].mean()
fatMaiorQueMedia = ''

for n in dados:
    if (n['valor']) != 0:
        if (n['valor']) > media:
           fatMaiorQueMedia += (str(n['dia']) + ' ')

print(f'O maior faturamento do mês foi: R$ {valorMax}.')
print(f'O menor faturamento do mês foi: R$ {valorMin}.')    
print(f'Os dias em que o faturamento foi maior que a média mensal foram: {fatMaiorQueMedia}')

