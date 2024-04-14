# import numpy as np
# import matplotlib.pyplot as plt
#
# # 定义信号函数
# def E(t):
#     return 50250 * (np.exp(-7.33e3*t) - np.exp(-1.23e7 * t))
#
# # 生成时间向量
# t = np.linspace(0, 0.01, num=1000)  # 时间从0到0.01秒，共1000个点
#
# # 计算信号
# y = E(t)
#
# # 计算FFT
# Y = np.fft.fft(y)
# freq = np.fft.fftfreq(len(y), t[1]-t[0])  # 计算频率
#
# # 绘制FFT曲线图
# plt.figure(figsize=(10, 6))
# plt.plot(freq[:len(freq)//2], np.abs(Y[:len(Y)//2]))  # 只绘制正频率部分
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')
# plt.title('FFT of E(t) Signal')
# plt.grid()
# print(1.23e7)
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
#
# # 定义信号函数
# def E(t):
#     return 50250 * (np.exp(-7.33e3 * t) - np.exp(-1.23e7 * t))
#
# # 生成时间向量
# t = np.linspace(0, 0.00005, num=1000)  # 时间从0到0.01秒，共1000个点
#
# # 计算信号
# y = E(t)
#
# # 绘制时域图
# plt.figure(figsize=(10, 6))
# plt.plot(t, y)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.title('Time Domain Plot of E(t) Signal')
# plt.grid()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
import  math

def E(x, alpha, beta, k):
    numerator = (beta - alpha) * k
    denominator = np.sqrt((alpha**2 + (x**2)) * (beta**2 + (x**2)))
    return np.abs(numerator / denominator)

# 设置参数值
alpha = 7330
beta = 12300000
k = 1.005

# 生成x的取值范围
x = np.linspace(0, 100, num=100)
# x = range(1000000)
x = 2*math.pi*x



# 计算信号
y = E(x, alpha, beta, k)

# 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('|E(x)|')
plt.title('Plot of |E(x)|')
plt.grid()
plt.show()

