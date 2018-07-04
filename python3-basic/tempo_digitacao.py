import matplotlib.pyplot as plt
import time

# legend
x = []
xLegend = []

# times to write a word
y = []

repeat = 7

word = "'abacate'"


print('Esse programa marcará o tempo gasto para digitar a palavra ' + word + '.Você terá que digitá-la ' + str(repeat) + ' vezes')
input('Aperte enter para começar')


for i in range(0, repeat):
    initialTime = time.clock()
    input('Digite um palavra:')
    finalTime = time.clock()
    y.append(round(finalTime - initialTime, 2))
    x.append(i + 1)
    xLegend.append(str(i + 1) + 'a vez')

plt.xticks(x, xLegend)
plt.plot(x, y)
plt.show()
