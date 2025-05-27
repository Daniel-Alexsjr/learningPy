import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import random

tamanho = int(input("Digite o tamanho do array: "))
sequencia = [random.randint(0, 1) for i in range(tamanho)]
tempo = list(np.arange(1, tamanho + 1))


x = tempo
y = sequencia


ax = plt.figure().gca()
ax.yaxis.set_major_locator(MaxNLocator(integer=True))


plt.step(x, y, color='orange', alpha=0.8)
plt.grid(axis='x', color='0.95')
plt.legend(title='very legal')
plt.title('frequencia de bit')

plt.show()