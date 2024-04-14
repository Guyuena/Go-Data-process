import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

config = {
    "font.family":'serif',
    "font.size": 12,
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
}
rcParams.update(config)
# 定义ReLU函数
def relu(x):
    return np.maximum(0, x)

# 定义ELU函数
def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

# 定义GELU函数
def gelu(x):
    cdf = 0.5 * (1.0 + np.tanh((np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3)))))
    return x * cdf

# 生成x轴数据
x = np.linspace(-5, 5, 100)

# 计算y轴数据
y_relu = relu(x)
y_elu = elu(x)
y_gelu = gelu(x)

# 绘制图形
plt.plot(x, y_gelu, label='GELU',color='red')
plt.plot(x, y_relu, label='ReLU',color='g')
plt.plot(x, y_elu, label='ELU')
# plt.yticks(fontproperties='Times New Roman', size=12)
# plt.xticks(fontproperties='Times New Roman', size=12)
plt.tick_params(axis='both',direction='in')
# plt.tick_params(axis='both',direction='in')

# 添加图例和标签
plt.legend()

plt.title('三种激活函数对比')


plt.savefig("GELU.svg", dpi=500)
# 展示图形
plt.show()