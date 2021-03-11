import matplotlib.pyplot as plt
import numpy as np

def graficar_isoclina(func, func_str):
    
    data = np.linspace(-15,15, 10)
    
    fig, ax = plt.subplots()
    ax.plot([-15,15],[0,0], color='black')
    ax.plot([0,0],[-15,15],  color='black')
    
    for j in range(-3,3):
        y = []
        for i in data:
            y.append(func(i))
        ax.plot(data,y, color = 'blue')
        ax.grid(b=True)
        ax.axis()
        ax.set_ylim(-15,15)
        ax.set_xlim(-15,15)
        ax.set_title(f"Isoclina de {func_str}")
    
    save_name = func_str.split(",")[0]
    fig.savefig(f'isoclina_{save_name}.png')
    
a = lambda x : - x
graficar_isoclina(a,"y'=x+y, y(0) = 0, k = 0")

b = lambda x : 2 * x - 8 
graficar_isoclina(b,"y'=2x-y, y(4) = 0, k = 8")