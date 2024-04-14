import numpy as np
import matplotlib.pyplot as plt

def silu(x):
    return x * (1 / (1 + np.exp(-x)))

x = np.linspace(-10, 10, 1000)
y = silu(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Silu Function')
plt.show()
