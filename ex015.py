salario= float (input('Digite o valor do seu salario para calcular o aumento : R$'))
aumento = salario + (salario * 15/100)

print('O valor do novo salario é de {:.2f}R$'.format(aumento))