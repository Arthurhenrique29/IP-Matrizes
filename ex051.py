#Crie um algoritmo que receba uma lista de números e retorne a soma de todos os elementos.
lista = input('Digite uma lista de números separados por espaço: ').split()
lista = [int(i) for i in lista]
soma = 0
for i in lista:
    soma += i
print(f'A soma de todos os elementos {lista} é igual: {soma}')
