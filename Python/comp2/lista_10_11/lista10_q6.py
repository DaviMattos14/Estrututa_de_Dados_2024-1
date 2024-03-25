import numpy as np
graus = (40*np.pi)/180
base = 8/np.tan(graus)
area = round((base*8)/2,4)
print(area)
