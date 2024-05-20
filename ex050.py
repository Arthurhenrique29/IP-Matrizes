#Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face.
n = int(input('Digite a quantidade de lançamentos: '))
contagem = [0] * 6
for i in range(n):
    resultado = int(input(f'Digite o resultado do lançamento {i+1}: '))
    if 1 <= resultado <= 6:
        contagem[resultado - 1] += 1
    else:
        print('Resultado inválido, digite um número entre 1 e 6,')
print('Número de ocorrências de cada face:')
for i in range(1,7):
    print(f'Face {i}: {contagem[i - 1]} ocorrências.')
