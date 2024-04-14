

import numpy as np
import tensorflow as tf
from PIL import Image
import math
"""
            将棋谱数据从npz文件中解析出来
"""
data = np.load('data1.npz')
print(data.files)
print(data["binaryInputNCHWPacked"].shape)
print(data["policyTargetsNCMove"].shape)

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
binhwc = tf.math.minimum(binhwc, tf.constant(1.0))  # 取出真正表示棋子的0-1数据
# print("binchwc= ",binhwc)
print("binchwc= ",binhwc.shape)
# print(binhwc[0])



# loc = tf.reshape(binhwc[0],[19,19,22])
loc = binhwc[999]
# print(loc.shape)
r  = loc[:,0:3]
print("r.shape",r.shape)
c=0
for i  in r[:,0]:
    if i!=0:
        c +=1
print(c)

X = tf.reshape(binhwc[999],[19,19,22])
# print(X)
print(X.shape)
y_2= tf.reduce_sum(X,2) #沿着轴1求和
img_y2  = tf.cast(y_2,tf.uint8)
print(img_y2)
img_y2=img_y2.numpy()
img_y2 = Image.fromarray(img_y2)




s0= r[:,0]*1   # 这个通道平面表示的是这个棋盘的形状，比如是19*19，那么就是全1矩阵， 而15*15，那么就是19*19的矩阵中只有15*15的1矩阵
s1= r[:,1]*128  # 己方的棋子
s2= r[:,2]*254  # 对手的棋子
ss = s0+s1+s2
print("ss.shape ",ss.shape)
ss = ss[:c]
print("ss.shape ",ss.shape)
size = math.sqrt(c)
print(size)
img = tf.reshape(ss,[int(size),int(size)])
img  = tf.cast(img,tf.uint8)
img2=img.numpy()
img2 = Image.fromarray(img2)
img2.show()
img_y2.show()


# print(ss2-ss)