#Lista Invertida: Crie um algoritmo que inverta uma lista de elementos.
lista = input('Digite uma lista de números separados por espaço: ').split()
lista = [int(i) for i in lista]
lista_invet = []
for i in range(len(lista) - 1, -1, -1):
    lista_invet.append(lista[i])
print(f'A lista invertida é {lista_invet}!')
