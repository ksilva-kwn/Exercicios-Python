prec= float (input('Digite o preço do produto para calcular o desconto : R$'))
desc = prec - (prec * 5 / 100)

print('O valor do produto que custa {:.2f}R$ com o desconto de 5% custará {:.2f}R$'.format(prec,desc))