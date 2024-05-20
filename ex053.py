#Média dos Elementos: Desenvolva um algoritmo que calcule e retorne a média dos elementos de uma lista de números.
lista = input('Digite uma lista de números separados por espaço: ').split()
lista = [int(i) for i in lista]
soma = 0
for i in lista:
    soma += i
media = soma / len(lista)
print(f'A média de todos os elementos da lista {lista} é igual {media:.2f}')