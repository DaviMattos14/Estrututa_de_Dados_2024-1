import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,5,0.1)
exponencial = np.exp(x)
linear = (25*x)-5
grau_3 = x**3 + x**2

plt.plot(x,exponencial, 'rs-', color='blue')
plt.plot(x,linear, '^-', color='green')
plt.plot(x,grau_3, 'ro-')
plt.legend(['Exponencial', 'Lienar', 'Terceiro Grau'], loc='best', shadow=True)
plt.show()
