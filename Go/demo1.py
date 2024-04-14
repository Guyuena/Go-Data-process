import matplotlib.pyplot as plt

board_size = 19

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

draw_board()
