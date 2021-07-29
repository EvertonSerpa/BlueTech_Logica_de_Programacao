'''02 - Calculadora de aumento de aluguel

Vamos construir um programa que irá calcular o aumento anual do seu aluguel em duas partes:

### Parte 1
A sua calculadora vai receber o `valor do aluguel` e calcular o aumento baseado no `IGPM de 31%`. A calculadora deve apresentar o aluguel reajustado no formato `R$ XXXX.XX`

**Exemplo:**
```
Valor do aluguel = 1000
Valor do aluguel reajustado = R$ 1310,00'''
print()
aluguel = float(input('Qaul o valor do seu aluguel? R$ '))
print()
igpm = aluguel * 31 / 100 + aluguel
print(f'O valor do seu aluguel é R$ {aluguel:.2f}\ncom o IGMP de 31% o novo valor fica R% {igpm:.2f}')
'''Explicando o código
Criei duas variveis, a primeira variavel recebe o valor do aluguel digitado pelo usuario.
A segunda variavel faz o calculo do aumento'''