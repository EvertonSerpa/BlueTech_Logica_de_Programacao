#02 - Escreva um programa que solicite uma frase ao usuário e escreva a frase 
# toda em maiúscula e sem espaços em branco.
print()
frase = input('Digite uma frase. ')
print(frase.upper()) # upper trasnforma toda a frase me maiúscula
print(frase.strip()) # strip retira os espaços das laterais
print(frase.replace(' ','')) # usei o replace para apagar todos os espaços embranco