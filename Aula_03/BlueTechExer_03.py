'''03 - Elabore um programa que recebe o seu nome, endereço e hobby e mostra cada uma das informações 
da seguinte forma:
- Nome -> Letra maiúscula
- Endereço -> Letra minúscula
- Hobby -> Primeira letra maiúscula'''
print()
Nome = input('Qual o seu nome? ').upper() # upper coloca todo o nome em letra maiúscula
Endereco = input('Qual o seu endereço? ').lower() # lower coloca todo o nome em letra minúscula
Hobby = input('Qual o seu hobby? ').capitalize() # capitaliza coloca a primeira letra em maiúscula
print()
print(f'{Nome}\n{Endereco}\n{Hobby}')