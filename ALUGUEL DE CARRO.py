dias = int(input('Quantos dias o carro foi usado? '))
k = float(input('Qual foi a quilometragem percorrida?' ))
diaria = (dias * 60) + (k * 0.15)
print('Portanto, a diária ficou em {}'.format(diaria))