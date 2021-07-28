# 5. **Menu** - Elabore um programa que mostre o seguinte menu na tela:
'''```
Cadastro de Clientes
0 - Fim
1 - Inclui
2 - Altera
3 - Exclui
4 - Consulta
Digite uma opção: 
```
Ao digitar um valor para a opção, o programa exibe qual opção foi escolhida.
```
Você escolheu a opção '0'.'''
print()
print('''Cadastro de Clientes:
0 - Fim
1 - Inclui
2 - Altera
3 - Exclui
4 - Consulta''')
opcao = int(input('Digite uma opção: '))
print()
print(f'Você escolheu a opção {opcao}.')
# Explicando o código
# Trabalhamos com o menu estatico, um campo para inserir qual valor o usuario escolhe
# e um print que vai printar as escolha do usuario na tela junto com a informação (Voê escolheu a opção x)