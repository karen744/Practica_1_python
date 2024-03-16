import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

rango = np.random.RandomState(0)
#x = np.linspace(0, 10 , 500)
#y = np.cumsum(rango.rand(500, 6), 0)
x_val = np.linspace(0, 10, 20)
y_val = x_val ** 2

plt.scatter(x_val, y_val)

sns.set()
 
#plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')


plt.show()