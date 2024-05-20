#Remover Elemento Específico: Escreva um algoritmo que remova todas as ocorrências de um elemento específico de uma lista. Portanto, o usuário deverá digitar qual elemento ele gostaria de retirar da lista, e o algoritmo deverá substituir cada ocorrência deste número por um asterisco “*”.
lista = input('Digite uma lista de números separados por espaço: ').split()
lista = [int(i) for i in lista]
print(f'Sua lista é {lista}!')
remover = (int(input('Qual número da lista você quer remover?: ')))
for i in range (len(lista)):
    if lista[i] == remover:
        lista[i] = '*'
print('A lista alterada é:', lista)