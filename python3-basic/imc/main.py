import imcUtils as imc

while True:
    sexo = input('Digite seu sexo (M-F):').lower()
    if sexo != 'm' and sexo != 'f':
        print('sexo deve ser (M ou F)')
    else:
        print('\n')
        break


while True:
    try:
        peso = float(input('Digite seu peso:'))
        if peso <= 0:
            print('Peso não pode ser negativo, ou zero.')
        else:
            print('\n')
            break
    except:
        print("Peso deve ser um número válido. separe kg de grama por '.'")


while True:
    try:
        altura = float(input('Digite seu altura:'))
        if altura <= 0:
            print('Altura não deve ser negativa, ou zero.')
        else:
            print('\n')
            break
    except:
        print("Altura deve ser um número válido. separe m de cm por '.'")

imc.classificacao(sexo, imc.imc(peso, altura))
