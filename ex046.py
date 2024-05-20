#Escreva um código similar à questão anterior, porém agora a figura deve ser vazia:
lado1 = int(input('Digite o valor do primeiro lado do retângulo (altura): '))
lado2 = int(input('Digite o valor do segundo lado do retângulo (base): '))
print('*' * lado2)
for i in range(lado1 - 2):
    print('*' + ' ' * (lado2 - 2) + '*')
if lado1 > 1:
    print('*' * lado2)