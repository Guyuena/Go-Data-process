import matplotlib.pyplot as plt
import numpy as np
import time

board_size = 19

# 模拟棋手思考的过程
def simulate_thinking():
    # 模拟思考过程
    for i in range(10):
        # 随机选择一个落子点
        x, y = np.random.randint(0, board_size), np.random.randint(0, board_size)
        # 更新图像
        plt.plot(x+0.5, y+0.5, 'ro', markersize=10)
        plt.pause(0.5)
        # 清空图像
        plt.clf()
        draw_board()

# 画出空的围棋棋盘
def draw_board():
    # 设置画布大小
    plt.figure(figsize=(8, 8))
    # 设置坐标轴范围
    plt.xlim([0, board_size])
    plt.ylim([0, board_size])
    # 绘制棋盘格线
    for i in range(board_size):
        plt.plot([i+0.5, i+0.5], [0.5, board_size-0.5], 'k')
        plt.plot([0.5, board_size-0.5], [i+0.5, i+0.5], 'k')
    # 绘制星位
    star_points = [(3,3), (9,3), (15,3), (3,9), (9,9), (15,9), (3,15), (9,15), (15,15)]
    for x, y in star_points:
        plt.plot(x, y, 'ko', markersize=5)
    # 隐藏坐标轴
    plt.axis('off')
    plt.show()
simulate_thinking()