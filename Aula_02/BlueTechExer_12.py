'''Parte 2
Agora, altere sua calculadora para receber além do `valor do aluguel`, o percentual do reajuste no formato `XX%`.  

**Dica:** Descubra uma forma de transformar o percentual recebido em um número para efetuar o cálculo.

**Exemplo:**
```
Valor do aluguel = 1000
Percentual do reajuste = 31%
Valor do aluguel reajustado = R% 1310,00'''
print()
aluguel = float(input('Qaul o valor do seu aluguel? R$ '))
igmp = float(input('Informe o valor do IGMP: '))
print()
calculo = aluguel * 31 / 100 + aluguel
print(f'O valor do seu aluguel é R$ {aluguel:.2f}\ncom o IGMP de {igmp} % o novo valor fica R% {calculo:.2f}')
'''Explicando o código
Foi criado três variveis, uma variavel recebe o valor do aluguel, a segunda recebe o valor do igpm
e a terceira faz o calculo'''