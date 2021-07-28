#Calcule os 10% do garçom de uma conta. 
print()
conta = float(input('Informe o valor da sua conta R$: '))
calculando = conta * 10 / 100 + conta
print(f'O valor da sua conta é: R$ {conta:.2f}, com os 10% do garçom ficou R$ {calculando:.2f}:') 
''''Explicando o Código
foi criado duas variaveis, a primeira variavel vai receber o valor em float = não inteiro. E a 
segunda variavel vai calcular os 10% do garçom. o print diz o valor da conta e mostra o valor já com os 10%
do garom. :.2f = formatação de quantas casas decimais eu quero que apareça'''