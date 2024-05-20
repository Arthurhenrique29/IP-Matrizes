# Desenvolva um algoritmo que remova os elementos duplicados de uma lista e retorne uma nova lista sem duplicatas.
lista = input('Digite uma lista de números separados por espaço: ').split()
lista = [int(i) for i in lista]
lista_nova = []
for i in lista:
    if i not in lista_nova:
        lista_nova.append(i)
print('A lista sem elementos duplicados é: ', lista_nova)
