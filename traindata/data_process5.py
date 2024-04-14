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
print("binhwc[0].shape= ",binhwc[0].shape)
# 和1.0比较，大于1.0的元素那么就是输出1.0，小于1.0的就输出源元素
binhwc = tf.math.minimum(binhwc, tf.constant(1.0))  # 取整张量元素中小于1的元素， 这样完成数据的0-1二值化表示
# print("binchwc= ",binhwc)
print("binchwc= ",binhwc.shape)
print("binhwc[0]= ",binhwc[0][21].shape)

X = tf.reshape(binhwc[0],[19,19,22])
# print(X)
print(X.shape)

y_2= tf.reduce_sum(X,2) #沿着轴1求和
print(y_2.shape)

print(y_2)



# f  = open("test.txt","w")
#
# for i in range(22):
#     res = X[:,:,i]
#     f.writelines(str(res))
#     f.write('\n')


