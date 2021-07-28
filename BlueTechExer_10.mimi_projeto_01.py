'''01 - Conversor de moedas

Crie um programa que solicite um um valor em real ao usuário e converta esse valor, para:

- DOLAR,
- EURO,
- LIBRA ESTERLINA,
- DÓLAR CANADENSE,
- PESO ARGENTINO,
- PESO CHILENO.

Para esse exercício você precisará realizar uma pesquisa para saber a cotação
 de cada moeda em real. Mostrar o resultado no formato $ XXXX.XX'''
print()
valor = float(input('Quanto em dinheiro você tem na sua carteira? '))
print()
dolar = valor / 5.11
euro = valor / 6.05
libra = valor / 7.11
dcanadense = valor / 4.08
pargentino = valor / 0.053
pchileno = valor / 0.0067 
# cotações do dia 28/07/2021
print(f'Com o valor de R$ {valor:.2f}\nvocê pode comprar:\nUSD {dolar:.2f} Dolares.\n€ {euro:.2f} Euros.\n£ {libra:.2f} Libras Esterlinas.\nCAD {dcanadense:.2f} Dólares Canadenses.\n$ {pargentino:.2f} Peso Argentino.\nCLP {pchileno:.2f} Peso Chileno.')
"""Explicando o código
cria as variaveis para cada moeda e faz a divisão entre o valor da moeda pelo valor do real. assim 
sabemos quanto de real compramos uma moeda x ou y"""