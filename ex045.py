#Escreva um código onde o usuário vai digitar o lado1 e o lado2 do retângulo e imprima este retângulo em formato de asteriscos.
lado1 = int(input('Digite o valor do primeiro lado do retângulo (altura): '))
lado2 = int(input('Digite o valor do segundo lado do retângulo (base): '))
print('*' * lado2)
for i in range(lado1):
    print('*' * lado2)