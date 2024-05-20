#Crie um programa que receba uma tupla de números e retorne duas tuplas, uma contendo os números pares e outra os números ímpares.
lista1 = input('Digite uma lista de números separados por espaço para a tupla 1: ').split()
lista1 = [int(i) for i in lista1]
tupla1 = ()
for i in lista1:
    tupla1 += (i,)
tupla_par = ()
tupla_impar = ()
for i in tupla1:
    if i % 2 == 0:
        tupla_par += (i,)
    else:
        tupla_impar += (i,)
print('A tupla com todos os número é: ', tupla1)
print('A tupla com os números pares é: ', tupla_par)
print('A tupla com os números ímpares é: ', tupla_impar)

