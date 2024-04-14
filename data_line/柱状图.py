# import matplotlib.pyplot as plt
#
# import random
#
# history = ["1998","2012","2014-1","2014-2","2015","2017"]
# acc = [10,20,30,40,50,60]
# la = ["LeNet","AlexNet","ZFNet","VGG","GoogleNet","ResNet","SENet"]
#
# x_data = ["{}年".format(i) for i in history]
# y_data = [random.randint(0, 100) for i in range(6)]
#
# plt.rcParams["font.sans-serif"] = ['SimHei']
# plt.rcParams["axes.unicode_minus"] = False
#
# for i in range(len(x_data)):
#     plt.bar(x_data[i], y_data[i])
#
# plt.title("CNN发展")
# plt.xlabel("时间")
# plt.ylabel("准确率")
#
# plt.show()

# import matplotlib.pyplot as plt
#
# # 构造数据
# X_set = [1, 2, 3, 4, 5]
# Y_set = [128, 211, 136, 234, 150]
# p1 = plt.bar(X_set, Y_set, width= 0.35, label='value')
# plt.bar_label(p1, label_type='edge')
# plt.title('The distribution of XXX')
# plt.show()

# import matplotlib.pyplot as plt
#
# # CNN的发展历史
# models = ['LeNet', 'AlexNet', 'VGG', 'GoogLeNet', 'ResNet', 'Inception', 'Xception']
# years = [1998, 2012, 2014, 2014, 2015, 2014, 2016]
# accuracies = [98.4, 84.7, 92.7, 93.3, 96.5, 93.9, 95.3]
#
# # 绘制柱状图
# plt.bar(models, accuracies)
#
# # 添加标签
# for i, model in enumerate(models):
#     plt.annotate(years[i], (model, accuracies[i]))
#
# # 添加标题和标签
# plt.title('Development of CNNs')
# plt.xlabel('Models')
# plt.ylabel('Accuracy (%!)(MISSING)')
#
# # 显示图像
# plt.show()

import matplotlib.pyplot as plt

# CNN的发展历史
models = ['LeNet', 'AlexNet', 'VGG', 'GoogLeNet', 'ResNet', 'Inception', 'Xception']
years = [1998, 2012, 2014, 2014, 2015, 2014, 2016]
accuracies = [98.4, 84.7, 92.7, 93.3, 96.5, 93.9, 95.3]

# 定义颜色
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

# 绘制柱状图
plt.bar(models, accuracies, color=colors)

# 添加标签
for i, model in enumerate(models):
    plt.annotate(years[i], (model, accuracies[i]))

# 添加标题和标签
plt.title('Development of CNNs')
plt.xlabel('Models')
plt.ylabel('Accuracy (%!!(MISSING))(MISSING)')

# 显示图像
plt.show()

