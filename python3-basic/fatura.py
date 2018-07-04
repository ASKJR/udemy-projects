fatura = []
totalFatura = 0
while True:
    produto = input('Digite o nome do produto: ')
    while True:
        preco = input('Digite o preço do produto: ')
        try:
            preco = float(preco)
            if preco <= 0:
                print('O preço não deve ser negativo')
            else:
                break
        except:
            print("Digie um numero valido e separe os centavos por '.'")
    fatura.append([produto, preco])
    totalFatura += preco
    continuar = input("Deseja continuar? Digite 's' para SIM, ou 'n' para NÃO.").lower()
    if (continuar == 'n'):
        break

for i in fatura:
    print(i[0], '-', i[1])
print('Total fatura:', totalFatura)
