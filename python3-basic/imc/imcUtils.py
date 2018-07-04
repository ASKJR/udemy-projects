def imc(peso, altura):
    return peso / (altura * altura)


def classificacao(sexo, imc):
    if sexo == 'f':
        if imc < 19.1:
            condicao = 'abaixo do peso'
        elif imc >= 19.1 and imc < 25.8:
            condicao = 'no peso normal'

        elif imc >= 25.8 and imc < 27.3:
            condicao = 'marginalmente acima do peso'

        elif imc >= 27.3 and imc < 32.3:
            condicao = 'acima do peso ideal'
        else:
            condicao = 'obeso'
    else:
        if imc < 20.7:
            condicao = 'abaixo do peso'
        elif imc >= 20.7 and imc < 26.4:
            condicao = 'no peso normal'

        elif imc >= 26.4 and imc < 27.8:
            condicao = 'marginalmente acima do peso'

        elif imc >= 27.8 and imc < 31.1:
            condicao = 'acima do peso ideal'
        else:
            condicao = 'obeso'
    imc = str(imc)
    print('Seu imc é:', imc[0:5], 'Sua classificação é:', condicao)
