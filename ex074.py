#Diferença entre Listas: Escreva uma função que receba duas listas como entrada e retorne uma nova lista contendo os elementos que estão presentes apenas em uma das listas, sem repetições.
lista1 = (input('Digite os elementos da lista 1 separados por espaço: ')).split()
lista1 = [int(i) for i in lista1]
lista2 = (input('Digite os elementos da lista 2 separados por espaço: ')).split()
lista2 = [int(i) for i in lista2]
unicos = []
for i in lista1:
    if i not in lista2:
        unicos.append(i)
for i in lista2:
    if i not in lista1:
        unicos.append(i)
print('Lista com elementos únicos: ', unicos)