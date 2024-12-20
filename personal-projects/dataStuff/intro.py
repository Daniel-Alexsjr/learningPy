import matplotlib.pyplot as plt
import numpy as np

tempo = np.linspace(0, 2*np.pi, 500)

y = np.cos(4*tempo)

plt.plot(tempo, y)
plt.title("gráfico do cosseno")
plt.xlabel("tempo (s)")
plt.ylabel("amplitude")
plt.show()