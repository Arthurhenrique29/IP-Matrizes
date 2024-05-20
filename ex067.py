#Desenvolva um programa que inverta uma tupla.
lista1 = input('Digite uma lista de números separados por espaço para a tupla 1: ').split()
lista1 = [int(i) for i in lista1]
tupla1 = ()
for i in lista1:
    tupla1 += (i,)
print('Tupla principal: ', tupla1)
tupla_invert = ()
for i in range(len(tupla1) - 1, -1, -1):
    tupla_invert += (tupla1[i],)
print('Tupla invertida: ', tupla_invert)