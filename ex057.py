#Ordenação: Escreva um programa que ordene uma lista de números em ordem crescente ou decrescente, dependendo do argumento passado para a função.
lista = input('Digite uma lista de números separados por espaço: ').split()
lista = [int(i) for i in lista]
ordem = (input('Escolha a ordem para a lista, "C" para crescente ou "D" para decrescente: '))
if ordem == 'C' or ordem == 'D' or ordem == 'c' or ordem == 'd':
    if ordem == 'C' or ordem == 'c':
        for i in range(1, len(lista)):
            chave = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > chave:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = chave
        print('Lista na ordem crescente:', lista)
    elif ordem == 'D' or ordem == 'd':
        for i in range(1, len(lista)):
            chave = lista[i]
            j = i - 1
            while j >= 0 and lista[j] < chave:
                lista[j + 1] = lista [j]
                j -= 1
            lista[j + 1] = chave
        print('Lista na ordem decrescente:', lista)
else:
    print('Opção inválida!')