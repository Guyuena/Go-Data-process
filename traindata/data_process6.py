
import numpy as np
import tensorflow as tf
from PIL import Image
"""
            将棋谱数据从npz文件中解析出来
"""
data = np.load('data1.npz')
print(data.files)
print(data["binaryInputNCHWPacked"].shape)
print(data["globalInputNC"].shape)
print(data["policyTargetsNCMove"].shape)
print(data["globalTargetsNC"].shape)
print(data["scoreDistrN"].shape)
print(data["valueTargetsNCHW"].shape)

# print(data["globalTargetsNC"][0])





binchwp = data["binaryInputNCHWPacked"]  # shape= [batch-size, num_plane ,packedBoardArea ]  [batch_size,num_bin_input_features,(pos_len*pos_len+7)//8])
bitmasks = tf.reshape(tf.constant([128, 64, 32, 16, 8, 4, 2, 1], dtype=tf.uint8), [1, 1, 1, 8])
# bitmasks结果： tf.Tensor([[[[128  64  32  16   8   4   2   1]]]], shape=(1, 1, 1, 8), dtype=uint8)
# print(bitmasks)
binchw = tf.reshape(tf.bitwise.bitwise_and(tf.expand_dims(binchwp, axis=3), bitmasks),
                    [-1, 22, ((19 * 19 + 7) // 8) * 8])
binchw = binchw[:, :, :19 * 19]
print("binchw= ",binchw.shape)
binhwc = tf.cast(tf.transpose(binchw, [0, 2, 1]), tf.float32)  #变为 [batch-size,22,361]  ---> [batch-size,361,22]
# print("binchwc= ",binhwc.shape)
# print("binchwc= ",binhwc)
# Returns the min of x and y (i.e. x < y ? x : y) element-wise.
print("binhwc[0]= ",binhwc[0][21])
# 和1.0比较，大于1.0的元素那么就是输出1.0，小于1.0的就输出源元素
binhwc = tf.math.minimum(binhwc, tf.constant(1.0))  # 取整张量元素中小于1的元素， 这样完成数据的0-1二值化表示
# print("binchwc= ",binhwc)
print("binchwc= ",binhwc.shape)
print("binhwc[0]= ",binhwc[0][21])















import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import PIL.Image as image
#读取原始图像
# paths ="img.png"
# X = plt.imread(paths)
# print("输入图像 X.shape ",X.shape)
# X = np.array(X)
# print("输入图像 X.shape ",X.shape)
X=binhwc[999][:,:3]
print(X.shape)
X= tf.reshape(X,[19,19,3])
print(X.shape)
X = np.array(X)
print(X.shape)
shape = row ,col ,dim =X.shape
X_ = X.reshape(-1,3)#(将矩阵化为2维，才能使用聚类)
#print(X_.shape)
def kmeans(X, n):
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(X)
    Y = kmeans.predict(X)
    return Y

plt.figure(1)  # 图像窗口名称
plt.subplot(2,3,1)
plt.imshow(X)
plt.axis('off')  # 关掉坐标轴为 off
plt.xticks([])
plt.yticks([])
plt.title("Picture")
for t in range(2, 7):
    index = '23' + str(t)
    plt.subplot(int(index))
    label = kmeans(X_,t)
    print("label.shape=",label.shape)
    # get the label of each pixel
    label = label.reshape(row,col)
    print("label new  shaep= ",label.shape)
    # create a new image to save the result of K-Means
    pic_new = image.new("RGB", (col, row))#定义的是图像大小为y*x*3的图像，这里列在前面行在后面
    for i in range(col):
        for j in range(row):
                if label[j][i] == 0:
                    pic_new.putpixel((i, j), (0, 0, 255))#填写的是位置为（j,i）位置的像素，列和行也是反的
                elif label[j][i] == 1:
                    pic_new.putpixel((i, j), (255, 0, 0))
                elif label[j][i] == 2:
                    pic_new.putpixel((i, j), (0, 255, 0))
                elif label[j][i] == 3:
                    pic_new.putpixel((i, j), (60, 0, 220))
                elif label[j][i] == 4:
                    pic_new.putpixel((i, j), (249, 219, 87))
                elif label[j][i] == 5:
                    pic_new.putpixel((i, j), (167, 255, 167))
                elif label[j][i] == 6:
                    pic_new.putpixel((i, j), (216, 109, 216))
    title = "k="+str(t)
    plt.title(title)
    plt.imshow(pic_new)
    plt.axis('off')  # 关掉坐标轴为 off
    plt.xticks([])
    plt.yticks([])

plt.show()


# kmeans步骤共可分为以下步骤：
#
#    1 随机初始化k个聚类中心。
#
#    2 计算所有像素点到聚类中心的距离。
#
#    3 选择最近的聚类中心作为像素点的聚类种类。
#
#    4 根据像素点的聚类种类更新聚类中心。
#
#    5 重复步骤2-4直至聚类中心收敛。