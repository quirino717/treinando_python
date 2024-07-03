km = float(input('\n\tO quão longe é o seu destino? '))

if km > 200:
    print('\n\tPara uma viagem de {}km\n\ta passagem custará  \033[1;32mR${:.2f}' .format(km, (km * 0.45)))
else:
    print('\n\tPara uma viagem de {}km\n\ta passagem custará  \033[1;32mR${:.2f}'.format(km, (km * 0.50)))