

import numpy as np
import tensorflow as tf
from PIL import Image
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

# r  = tf.reduce_sum(binhwc[0],-1)
# print(r)
# rr = tf.reshape(r,[19,19])
# print(rr)

# loc = tf.reshape(binhwc[0],[19,19,22])
loc = binhwc[999]
# print(loc.shape)
r  = loc[:,0:3]
# print(loc[:,0:3])
r1 = tf.reshape(loc[:,0:3],[19,19,3])
loc2 = binhwc[1000]
# print(loc.shape)
rr  = loc2[:,0:3]
# print(loc[:,0:3])
r2 = tf.reshape(loc2[:,0:3],[19,19,3])
# print(r1.shape)
# print(len(binhwc[0][0]))
# for i  in binhwc[0][0]:
#     print(i)
# print(len(r[:,0]))
# for i in r[:,1]:
#     if i==1.0:
#         i=128
# print(r[:,1]*100)

#  只取22个通道的前3个表示棋盘有子和颜色的通道，进行反向表征为一个棋盘图像

# s0= (r[:,0]*1).numpy()
# print(s0)
# s1= (r[:,1]*254).numpy()
# print(s1)
# s2= (r[:,2]*254).numpy()
# print(s2)
# ss = np.logical_and(s0,s1,s2,)
# print(ss)
s0= r[:,0]*1   # 这个通道平面表示的是这个棋盘的形状，比如是19*19，那么就是全1矩阵， 而15*15，那么就是19*19的矩阵中只有15*15的1矩阵
# print("s0=",s0)
s1= r[:,1]*128  # 己方的棋子
# print("s1=",s1)
s2= r[:,2]*254  # 对手的棋子
# print("s2=",s2)
ss = s0+s1+s2
img = tf.reshape(ss,[19,19])
# print(img)
img  = tf.cast(img,tf.uint8)
# print(img)
img2=img.numpy()
img2 = Image.fromarray(img2)
img2.show()

s20= rr[:,0]*1
s21= rr[:,1]*128
s22= rr[:,2]*254
ss2 = s20+s21+s22
# img22 = tf.reshape(ss2,[19,19])
img22 = ss2
# print(img22)
img22  = tf.cast(img22,tf.uint8)
# print(img22)
img22=img22.numpy()
img22 = Image.fromarray(img22)
img22.show()

# print(ss2-ss)