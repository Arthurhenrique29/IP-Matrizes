#Crie um programa que receba uma lista de palavras e conte quantas vezes cada vogal aparece no total.
lista = input('Digite algo: ')
letras = []
for i in lista:
    letras.append(i)
print(letras)
cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0
for i in letras:
    if i == 'a':
        cont_a += 1
    elif i == 'e':
        cont_e += 1
    elif i == 'i':
        cont_i += 1
    elif i == 'o':
        cont_o += 1
    elif i == 'u':
        cont_u += 1
print('Contagem das vogais:')
print('A:', cont_a)
print('E:', cont_e)
print('I:', cont_i)
print('O:', cont_o)
print('U:', cont_u)