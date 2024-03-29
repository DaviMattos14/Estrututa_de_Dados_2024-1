'''
    Nome: Davi dos Santos Mattos    DRE: 119133049
'''
import numpy as np
import matplotlib.pyplot as plt

"""
    QUESTÃO 1
"""

x = np.arange(0,5,0.1)
exponencial = np.exp(x)
linear = (25*x)-5
grau_3 = x**3 + x**2

plt.plot(x,exponencial, 'rs-', color='blue')
plt.plot(x,linear, '^-', color='green')
plt.plot(x,grau_3, 'ro-')
plt.legend(['Exponencial', 'Lienar', 'Terceiro Grau'], loc='best', shadow=True)
plt.show()

"""
    QUESTÃO 2
"""
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

"""
    QUESTÃO 3
"""
x = np.arange(0,2,0.05)

fun1 = np.sin((25*x)/2) - np.sin((63*x)/10)
fun2 = ((-13*x)+15)/10
plt.subplot(121)
plt.plot(x, fun1, '^-', color='green')
plt.plot(x, fun2, 'b--')

plt.subplot(122)
plt.fill_between(x,fun1,fun2,color='y')
plt.show()

"""
    QUESTÃO 4
"""

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