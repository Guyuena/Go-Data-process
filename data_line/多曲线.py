import matplotlib.pyplot as plt
import numpy as np


plt.rc('font',family='Times New Roman',size=12) # Times New Roman字体设置


# 2.绘制一张空白图
fig, ax = plt.subplots() # 创建图实例
x = np.linspace(0,2,100) # 创建x的取值范围
y1 = x
ax.plot(x, y1, label='linear') # 作y1 = x 图，并标记此线名为linear
y2 = x ** 2
ax.plot(x, y2, label='quadratic') #作y2 = x^2 图，并标记此线名为quadratic
y3 = x ** 3
ax.plot(x, y3, label='cubic') # 作y3 = x^3 图，并标记此线名为cubic
ax.set_xlabel('x label') #设置x轴名称 x label
ax.set_ylabel('y label') #设置y轴名称 y label
ax.set_title('Simple Plot') #设置图名为Simple Plot
ax.legend() #自动检测要在图例中显示的元素，并且显示

plt.show() #图形可视化

