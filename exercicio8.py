distancia = float(input('Informe uma distancia em metros: '))

km = distancia/1000
hm = distancia/100
dam = distancia/10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

print('\nConvertendo o valor de {}m temos: \n'
      '{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm\n'
      .format(distancia, km, hm, dam, dm, cm, mm))