dicionarioCores = {'vermelho': 'red', 'amarelo': 'yellow', 'verde': 'green', 'azul': 'blue'}
cor = input('Digite uma cor: ').lower()
print(dicionarioCores.get(cor, 'Esta cor não consta no meu dicionário'))
input('Aperte enter para encerrar...')
