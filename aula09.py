frase = 'Curso em Vídeo Python'

print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[0:20:2])
print(frase.count('e'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(frase.lower().count('o'))
print(frase.upper())
print(frase.lower())
print(frase.title())
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase.find('Curso'))

frase = frase.replace('Curso em Vídeo Python', 'prova de python')
print(frase)
print(len(frase))

dividido = frase.split()
print(dividido)
print(dividido[0])