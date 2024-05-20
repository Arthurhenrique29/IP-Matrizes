#Escreva um programa que receba duas listas, uma com os valores das notas e outra com os pesos correspondentes, e calcule a média ponderada.
notas = input('Digite as notas separadas por espaço: ').split()
notas = [float(i) for i in notas]
pesos = input('Digite os pesos correspondentes separados por espaço: ').split()
pesos = [float(i) for i in pesos]
if len(notas) != len(pesos):
    print('O número de notas deve ser igual ao número de pesos!')
else:
    soma_notas = 0
    soma_pesos = 0
    for i in range(len(notas)):
        soma_notas += notas[1] * pesos[i]
        soma_pesos += pesos[i]
media = soma_notas / soma_pesos
print('A média aritmética ponderada é: ', media)