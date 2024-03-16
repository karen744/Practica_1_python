import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

rango = np.random.RandomState(0)
#x = np.linspace(0, 10 , 500)
#y = np.cumsum(rango.rand(500, 6), 0)
#x_val = np.linspace(0, 10, 20)
#y_val = x_val ** 2

#plt.plot(x_val, y_val, color='r')
#plt.scatter(x_val, y_val, marker=',', color='g')
#plt.title("dezplazamiento")
#plt.xlabel("Tiempo [segundos]")
#plt.ylabel("Distancia [metros]")

#sns.set()

data = np.random.multivariate_normal([0, 0], [[2, 5], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])


for col in "xy":
    sns.kdeplot(data[col], shade = True)

for col in 'xy':
    sns.histplot(data[col], alpha = 0.5, kde = False)
    iris = sns.load_dataset("iris")

iris.head()
sns.pairplot(iris, hue='species', size=2.5)
 
#plt.plot(x, y)
#plt.legend('ABCDEF', ncol=2, loc='upper left')


plt.show()