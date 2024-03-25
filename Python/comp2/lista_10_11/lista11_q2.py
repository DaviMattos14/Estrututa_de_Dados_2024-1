import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)

fun1 = np.exp(-x/2) * np.sin(2*np.pi*x)
fun2 = np.cos(x/2)

plt.subplot(211)
plt.plot(x,fun1, 'b-')
plt.plot(x,fun2, 'r-')
plt.grid(True, linestyle='--')
#plt.show()

dif = fun2-fun1
plt.subplot(212)
plt.bar(x+0.04, dif, 0.05, color='r')
plt.bar(x, dif, 0.05, color='black')
plt.show()