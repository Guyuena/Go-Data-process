import numpy as np
import matplotlib.pyplot as plt


config = {
    "font.family":'serif',
    "font.size": 12,
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
}
def swish(x):
    return x * sigmoid(x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-10, 10, 100)
y = swish(x)

plt.plot(x, y)
plt.tick_params(axis='both',direction='in')
# plt.xlabel('x')
# plt.ylabel('y')
plt.title('Swish')
plt.show()
