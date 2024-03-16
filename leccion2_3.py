import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

rango = np.random.RandomState(0)
#x = np.linspace(0, 10 , 500)
#y = np.cumsum(rango.rand(500, 6), 0)
x_val = np.linspace(0, 10, 20)
y_val = x_val ** 2

plt.plot(x_val, y_val, color='r')
plt.scatter(x_val, y_val, marker=',', color='g ')
plt.title("dezplazamiento")
plt.xlabel("Tiempo [segundos]")
plt.ylabel("Distancia [metros]")

sns.set()
 
#plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')


plt.show()