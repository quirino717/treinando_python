temp = int(input('Digite 1 para converter Celsius para Fahrenheit\nDigite 2 para converter Fahrenheit para Celsius\nO que deseja fazer: '))

if temp == 1:
    celsius = float(input('\nDigite a temperatura em °C: '))

    print('\n{}°C equivalem a {:.2f}°F' .format(celsius,(celsius*(9/5)+32)))

if temp == 2:
    fahrenheit = float(input('\nDigite a temperatura em °F: '))

    print('\n{}°F equivalem a {:.2f}°C' .format(fahrenheit,(fahrenheit-32)/(9/5)))