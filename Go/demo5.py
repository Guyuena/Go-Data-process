# import matplotlib.pyplot as plt
# import numpy as np
#
# # 模拟训练过程中的数据
# epochs = 50
# train_loss = np.random.rand(epochs) * 0.5
# train_acc = np.random.rand(epochs) * 0.4 + 0.6
# val_loss = np.random.rand(epochs) * 0.4 + 0.3
# val_acc = np.random.rand(epochs) * 0.2 + 0.8
#
# # 绘制训练集和验证集的损失曲线
# plt.plot(range(epochs), train_loss, label='Train Loss')
# plt.plot(range(epochs), val_loss, label='Val Loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.title('Training and Validation Loss')
# plt.legend()
# plt.show()
#
# # 绘制训练集和验证集的准确率曲线
# plt.plot(range(epochs), train_acc, label='Train Acc')
# plt.plot(range(epochs), val_acc, label='Val Acc')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.title('Training and Validation Accuracy')
# plt.legend()
# plt.show()



import matplotlib.pyplot as plt

# 模拟训练过程中的数据
model1_acc = [0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.92, 0.93, 0.94]
model2_acc = [0.6, 0.65, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.83]
model3_acc = [0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85]

# 绘制多个模型的训练精度曲线
plt.plot(model1_acc, label='Model 1')
plt.plot(model2_acc, label='Model 2')
plt.plot(model3_acc, label='Model 3')

plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training Accuracy')
plt.legend()
plt.show()
