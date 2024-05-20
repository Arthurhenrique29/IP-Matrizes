#Escreva um programa que ordene uma lista de números de forma que os elementos se alternem entre o maior e o menor valor.
lista = input('Digite uma lista de números separados por espaço: ').split()
lista = [int(i) for i in lista]
for i in range(1, len(lista)):
    chave = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > chave:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = chave
print('Lista na ordem crescente:', lista)
nova_lista = []
inicio = 0
fim = len(lista) - 1
while inicio <= fim:
    if fim > inicio:
        nova_lista.append(lista[fim])
    nova_lista.append(lista[inicio])
    inicio += 1
    fim -= 1
print('A lista alternada entre maior e menor: ', nova_lista)
