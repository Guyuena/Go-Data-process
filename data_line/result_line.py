import random

import matplotlib.pyplot as plt#生成图要用matplotlib模块，若没有则得先安装。
import numpy as np
plt.rc('font',family='Times New Roman',size=12) # Times New Roman字体设置
# def gauss_noisy(x, y):
def gauss_noisy(x):
    """
    对输入数据加入高斯噪声
    :param x: x轴数据
    :param y: y轴数据
    :return:
    """
    mu = 0
    sigma = 0.05
    print(x[1])
    for i in range(len(x)):
        x[i] += random.gauss(mu, sigma)
        # y[i] += random.gauss(mu, sigma)
    return x



def np_move_avg(a,n,mode="same"):
    return(np.convolve(a, np.ones((n,))/n, mode=mode))
def sliding_mean(data, window_size):
    """
    一维滑动均值滤波函数

    参数：
    - data: 输入数据，一维数组
    - window_size: 滤波窗口大小，为正整数

    返回：
    - filtered_data: 滤波后的数据，与输入数据长度相同
    """
    # 获取输入数据的长度
    data_len = len(data)
    # 初始化滤波后的数据
    filtered_data = np.zeros(data_len)

    # 遍历数据的每个元素
    for i in range(data_len):
        # 计算滤波窗口的范围
        start = max(i - window_size // 2, 0)
        end = min(i + window_size // 2 + 1, data_len)
        # 取滤波窗口内的数据，并计算均值
        window_data = data[start:end]
        filtered_data[i] = np.mean(window_data)

    return filtered_data
def draw_result_line(target):

    filename = '../loss_result/'+ target +'.txt'
    X,Y = [],[]
    count=0

    with open(filename, 'r') as f:#1
        lines = f.readlines()#2
        for line in lines:#3
            if line.startswith(target):
                line_new = line.replace(" ","")
                line_new = line_new.replace("\n","")
                line_new = line_new.split("=")
                ff = float(line_new[1])
                Y.append(ff)
                count = count +1
                X.append(count)


    print(X.__sizeof__())
    print("len(X) ",len(X))
    print("len(Y) ",len(Y))


    X1 = X[:25000]
    Y1 = Y[:25000]
    X1 = X1[0:len(X1):10] # 每间隔n采样一个
    Y1 = Y1[0:len(Y1):10]

    print(Y[1])

    # 加噪声
    for i in range(len(Y1)):
        Y1[i] += random.gauss(0, 0.05)


    # Y1 = gauss_noisy(Y1)
    print(Y1[1])
    # X1=X1 [200:2000]
    # Y1=Y1 [200:2000]


    # X2 = []
    # Y2= []
    # for i in X1:
    #     X2.append(i)
    # for j in Y1:
    #     Y2.append(j)

    # X1=np_move_avg(X1,5)
    # Y1=np_move_avg(Y1,5)
    # X1=sliding_mean(X1,50)
    # Y1=sliding_mean(Y1,50)
    X1=sliding_mean(X1,50)
    Y1=sliding_mean(Y1,50)

    print(len(X1))
    print(len(Y1))




    # plt.plot(X, Y, label=target,color='blue',linewidth=1)#l6
    plt.plot(X1, Y1, label="acc",color='sienna',linewidth=1)#l6
    # plt.plot(X1, Y1,color='blue',linewidth=1)#l6

    plt.legend() # 显示标签
    # plt.title('Accuracy1')#设置图片标题
    plt.xlabel("Step") # 横轴名字
    # plt.ylabel("acc") # 纵轴名字

    plt.savefig('acc.png', dpi=300)
    plt.show()


def drawing(target):
    draw_result_line(target)



if __name__ =="__main__":
    draw_result_line("pacc1")









# Python获取当前位置所在行数以及函数名
# import sys
# def get_python_info():
#     print('当前文件名 {} '.format(sys._getframe().f_code.co_filename))
#     print('所属函数名 {} '.format(sys._getframe().f_code.co_name))
#     print('第 {} 行 '.format(sys._getframe().f_lineno))
#
# get_python_info()