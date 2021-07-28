'''Qual o valor do troco?

*   Defina uma variável para o valor de uma compra que custou R$100,98;

*   Defina uma variável para o valor que o cliente pagou R$150,00;

*   Defina uma variável que calcula o valor do troco e exiba-o no console com o valor final arredondado.'''
print()
compra = 100.98
pagou = 150.00
troco = pagou - compra
print(f'O valor do seu troco é: R$ {troco:.1f}')
# Explicando o código
'''variavel compra recebe o valor 100.98
variavel pagou recebe o valor 150.00
e a variavel troco faz uma subtração
print uso uma fstring com a formatação :.1f'''