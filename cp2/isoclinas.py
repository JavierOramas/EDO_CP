import matplotlib.pyplot as plt
import numpy as np

data = np.linspace(-5,5, 10)

func = lambda x, k: -x + k 

for j in range(-3,3):
    y = []
    for i in data:
        y.append(func(i,j))
    plt.plot(data,y)
    plt.legend([f'k={item}' for item in range(-3,3)])
    plt.grid(b=True)
    plt.axis()
plt.savefig('isoclinas_a.png')