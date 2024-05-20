#Escreva um algoritmo que encontre e retorne o maior elemento em uma lista de números.
lista = input('Digite uma lista de números separados por espaço: ').split()
lista = [int(i) for i in lista]
maior = lista[0]
for i in lista:
    if i > maior:
        maior = i
print(f'O maior elemento da lista {lista} é {maior}!')