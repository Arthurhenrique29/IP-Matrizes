#Dada uma sequência de n números, imprimi-la na ordem inversa à da leitura.
n = int(input('Digite a quantidade de números na sequência: '))
seq = []
for i in range(n):
    numero = int(input(f'Digite o número {i+1}: '))
    seq.append(numero)
print('Sequencia na ordem inversa:')
for i in range(n-1,-1,-1):
    print(seq[i])
