'''Calculadora de Dano** - Escreva um programa que receba dois valores digitados pelo usuário:
  - Quantidade de vida de um monstro (entre 10 e 50);
  - Valor do ataque do jogador por turno (entre 5 e 10);
  - Baseado nos valores digitados, exiba a quantidade de turnos que o jogador irá demorar para conseguir derrotar o monstro.
  - ```
    O jogador irá derrotar o monstro em 8 turnos.'''

print()
print('JOGO DO GUABIRU\n\nNa sua casa tem um guabiru, vamos escolher a quantidade de vida do (Jerry) no campo vida\ne o ataque do (Tom) no campo ataque, para ver em quantas rodadas o Tom coloca o Jerry para fora de casa. ')
print()
valor_vida = float(input('Vida, escolha um número entre: [10 e 50]: '))
valor_ataque = float(input('Ataque, escolha um número entre: [5 e 10]: '))
turnos = valor_vida / valor_ataque
print()
print(f'O Tom irá derrotar o Jerry em {turnos:.1f} turno(s). ')
# Explicando o código
'''A primeira vista parece ser complicado, mas se trata da uma divisão. Criei 3 variveis onde 
a variavel valor_vida recebe a quantidade de vida do Jerry e a variavel valor_ataque recebe a 
quantidade de ataque do Tom. Como eu quero saber em quantos turnos o Tom vai derrotar o Jerry
e só dividir valor_vida por valor_ataque que temos o resultado. A variavel turnos faz a divisão. '''