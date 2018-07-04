'''
 Developer : Alberto Kato
 Cálculo salário líquido CLT
 tabela para cálculos (2018):
 	http://www.calculador.com.br/tabela/trabalhista/IRRF/2015
 	http://www.calculador.com.br/tabela/trabalhista/INSS/2018
'''
def getInssDiscount(salary):
    if salary <= 1693.72:
        return ['8%', round(0.08 * salary, 2)]
    elif salary >= 1693.73 and salary <= 2822.90:
        return ['9%', round(0.09 * salary, 2)]
    elif salary >= 2822.91 and salary <= 5645.80:
        return ['11%', round(0.11 * salary, 2)]
    else:
        return ['11%', round(0.11 * 5645.80, 2)]


def getIRRFDiscout(salary, numberOfDependents):
    if numberOfDependents > 0:
        salary = salary - (numberOfDependents * valorDeducaoPorDependente)

    if salary <= 1903.98:
        return ['isento', 0]
    elif salary >= 1903.99 and salary <= 2826.65:
        return ['7.5%', round((salary * 0.075) - 142.80, 2)]
    elif salary >= 2826.66 and salary <= 3751.05:
        return ['15%', round((salary * 0.15) - 354.80, 2)]
    elif salary >= 375.06 and salary <= 4664.68:
        return ['22.50%', round((salary * 0.225) - 636.13, 2)]
    else:
        return ['27.50%', round((salary * 0.275) - 869.36, 2)]


def getUserSalary():
    while True:
        salary = input('Digite seu salário bruto:')
        try:
            salary = float(salary)
            if salary < currentMinSalary:
                print('Salário inferior ao salário Mínimo R$' + str(currentMinSalary))
            else:
                return salary
        except:
            print("Digite um valor válido para o salário. Utilize '.' para separar os centavos.")


def getDependentsNumber():
    while True:
        dependents = input('Digite número de dependentes:')
        try:
            dependents = int(dependents)
            if dependents < 0:
                print('Digite um número >= 0')
            else:
                return dependents
        except:
            print("Digite um número inteiro válido.")


def getOtherDiscounts():
    while True:
        otherDiscounts = input('Digite o valor de outros descontos:')
        try:
            otherDiscounts = float(otherDiscounts)
            if otherDiscounts >= currentMinSalary:
                print('Descontos maiores que os proventos')
            else:
                return otherDiscounts
        except:
            print("Digite um valor válido para o desconto. Utilize '.' para separar os centavos.")


def getTotalDiscounts(grossSalary, dependents, otherDiscounts):
    discount = 0
    inssDiscount = getInssDiscount(grossSalary)
    discount += inssDiscount[1]
    irffDiscout = getIRRFDiscout(grossSalary - discount, dependents)
    discount += irffDiscout[1]
    discount += otherDiscounts
    return {'INSS': [inssDiscount[0], inssDiscount[1]],
            'IRRF': [irffDiscout[0], irffDiscout[1]], 'OTHER': otherDiscounts, 'TOTAL': discount}


def printPayCheck(grossSalary, discountDictionary):
    headerAndFooter = '#'

    for i in range(1, 50):
        headerAndFooter += '#'

    print(headerAndFooter)
    print('Salário base: R$' + str(grossSalary) + '\n')
    print('INSS desconto de ' + str(discountDictionary['INSS'][0]) + ' : R$' + str(discountDictionary['INSS'][1]) + '\n')
    print('IRFF desconto de ' + str(discountDictionary['IRRF'][0]) + ' : R$' + str(discountDictionary['IRRF'][1]) + '\n')
    print('Outros descontos: R$' + str(discountDictionary['OTHER']) + '\n')
    print('Total de descontos: R$' + str(salaryDiscounts['TOTAL']) + '\n')
    print('Salário líquido: R$' + str(round(grossSalary - salaryDiscounts['TOTAL'], 2)) + '\n')
    print(headerAndFooter)



# Const values
currentMinSalary = 954.00
valorDeducaoPorDependente = 189.59

print('-------------------Cálculo Salário Líquido-------------------')

while True:
        # User input values
    grossSalary = getUserSalary()
    dependents = getDependentsNumber()
    otherDiscounts = getOtherDiscounts()

    salaryDiscounts = getTotalDiscounts(grossSalary, dependents, otherDiscounts)

    printPayCheck(grossSalary, salaryDiscounts)
    stay = input('Deseja realizar outro Cálculo? (S ou N) : ').lower()
    if stay == 'n':
        break
