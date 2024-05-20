#Elementos Únicos: Crie um algoritmo que retorne uma lista com os elementos que aparecem em apenas uma das duas listas passadas como argumento.
lista1 = [1,3,4,6,7,8,9]
lista2 = [1,2,5,6,8,10]
unicos = []
for i in lista1:
    if i not in lista2:
        unicos.append(i)
for i in lista2:
    if i not in lista1:
        unicos.append(i)
print('Lista com elementos únicos: ', unicos)
