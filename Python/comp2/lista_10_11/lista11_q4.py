import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2,0.01)

fun1 = np.sin((25*x)/2)
fun2 = np.sin((63*x)/10)

plt.subplot(211)
plt.plot(x, fun1, 'g-')
plt.plot(x, fun2, 'r-')

plt.subplot(212)
plt.fill_between(x, fun1, fun2, where=fun1>fun2, color="green")
plt.fill_between(x, fun1, fun2, where=fun1<fun2, color="red")
plt.show()