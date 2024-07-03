import math

ang = float(input('Informe um ângulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('\nO ângulo {}° tem\nseno de {:.2f}°,\ncosseno de {:.2f}°\ntangente de {:.2f}°' .format(ang, sen, cos, tan))