medida= float (input('Digite a distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida/10
hm = medida/100
km = medida/1000
print('A medida de {} metros é igual a {:.0f} centrímetros'.format(medida,cm))
print('A medida de {} metros é igual a {:.0f} milímetros'.format(medida, mm))
print('A medida de {} metros é igual a {:.0f} decímetros'.format(medida, dm))
print('A medida de {} metros é igual a {} decâmetros'.format(medida, dam))
print('A medida de {} metros é igual a {} hectômetros'.format(medida, hm))
print('A medida de {} metros é igual a {} quilômetros'.format(medida, km))