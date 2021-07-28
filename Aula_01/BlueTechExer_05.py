# 05 - Elabore um programa que receba 4 notas de um aluno e calcule a média dele.
print()
nota01 = float(input('Digite a primeira nota do aluno: '))
nota02 = float(input('Digite a segunda nota do aluno: '))
nota03 = float(input('Digite a terceira nota do aluno: '))
nota04 = float(input('Digite a quarta nota do aluno '))
media = (nota01 + nota02 + nota03 + nota04) / 4
print()
print(f'A primeira nota: {nota01}\nA segunda nota: {nota02}\nA terceira nota: {nota03}\nA quarta nota: {nota04}\nE A média: {media}')

# Explicando o código
# Foi criado 4 variaveis para notas, onde cada variavel recebe um valor de uma nota especifica.
# a variavel média calcula a média final do aluno. 
# o print formatado apresesnta as informações das notas e média. \n = quebra de linha.
