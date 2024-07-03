nota1 = float(input('\n\tDigite a primeira nota: '))
nota2 = float(input('\tDigite a segunda nota: '))

media = (nota1 + nota2) / 2

print('\n\tVocê obteve uma média de {:.1f}' .format(media))

if media < 5:
    print('\n\tVocê foi \033[31mREPROVADO!!\033[m')
elif 5 <= media < 6.9:
    print('\n\tVocê \033[33mestá de recuperação!!\033[m')
else:
    print('\n\tVocê foi \033[32mAPROVADO!!\033[m\n\tNão fez mais que sua obrigação')