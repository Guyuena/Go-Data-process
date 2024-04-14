import matplotlib.pyplot as plt

# 模拟模型准确率缓慢上升但不超过40%
epochs = list(range(1, 501))

accuracy = [i * 0.08 for i in epochs]
# accuracy = [acc if acc <= 0.4 else 0.4 for acc in accuracy]

# 绘制曲线
plt.plot(epochs, accuracy)
plt.title('Model Accuracy over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.show()
