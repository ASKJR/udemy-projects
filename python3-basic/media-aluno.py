# total de aulas = 20
# Aprovado mínimo 70% de presença && média >=6
nome = input('Digite seu nome: ')

# validação input
while True:
    p1 = input('Digite a nota da P1: ')
    try:
        p1 = float(p1)
        if p1 >= 0 and p1 <= 10:
            break
        else:
            print('Nota deve ser ente 0-10')
    except:
        print('Digite um número válido para nota')
while True:
    p2 = input('Digite a nota da P2: ')
    try:
        p2 = float(p2)
        if p2 >= 0 and p2 <= 10:
            break
        else:
            print('Nota deve ser ente 0-10')
    except:
        print('Digite um número válido para nota')

while True:
    totalFaltas = input('Digite o número de faltas: ')
    try:
        totalFaltas = int(totalFaltas)
        if totalFaltas >= 0 and totalFaltas <= 20:
            break
        else:
            print('Número de faltas deve ser entre 0-20')
    except:
        print('Digite um número válido para o número de faltas')

media = (p1 + p2) / 2
assiduidade = ((20 - totalFaltas) * 100) / 20

if assiduidade < 70 and media < 6:
    resultado = 'Reprovado por faltas e por média'

elif assiduidade < 70:
    resultado = 'Reprovado por faltas'

elif media < 6:
    resultado = 'Reprovado por média'

else:
    resultado = 'Aprovado'

print('Nome:', nome)
print('Média:', media)
print('Percentual de presença (assiduidade):', assiduidade, '%')
print('Resultado:', resultado)
