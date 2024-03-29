import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2,0.05)

fun1 = np.sin((25*x)/2) - np.sin((63*x)/10)
fun2 = ((-13*x)+15)/10
plt.subplot(121)
plt.plot(x, fun1, '^-', color='green')
plt.plot(x, fun2, 'b--')

plt.subplot(122)
plt.fill_between(x,fun1,fun2,color='y')
plt.show()