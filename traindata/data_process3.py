
import numpy as np
import tensorflow as tf
from PIL import Image
"""
            将棋谱数据从npz文件中解析出来  
            解析价值评估数据 globalTargetsNC
  //C0-3: Categorial game result, win,loss,noresult, and also score. Draw is encoded as some blend of win and loss based on drawEquivalentWinsForWhite.
  // 游戏结果的分类，赢、输、无结果，还有分数。平局被编码为基于平局的赢和输的某种混合。
"""
data = np.load('data1.npz')
print(data.files)
print(data["globalTargetsNC"].shape)

value  = data["globalTargetsNC"][:,0:3]
print(value.shape)

print(value[0:20])
# policy = data["policyTargetsNCMove"]
# # print(policy)
# policy_target0 = data["policyTargetsNCMove"][:, 0, :]
# print("policy_target0.shape=" ,policy_target0.shape)
# policy_target0 = policy_target0 / tf.reduce_sum(policy_target0, axis=1, keepdims=True)
# print("policy_target0[1000]= " ,policy_target0[999])
# print(np.argmax(policy_target0[999].numpy()))
#
#
#
# policy_target1 = data["policyTargetsNCMove"][:, 1, :]
# policy_target1 = policy_target1 / tf.reduce_sum(policy_target1, axis=1, keepdims=True)
# # print("policy_target1[0]= ",policy_target1[100])
#
#
#
# binchwp = data["binaryInputNCHWPacked"]  # shape= [batch-size, num_plane ,packedBoardArea ]  [batch_size,num_bin_input_features,(pos_len*pos_len+7)//8])
# bitmasks = tf.reshape(tf.constant([128, 64, 32, 16, 8, 4, 2, 1], dtype=tf.uint8), [1, 1, 1, 8])
# # bitmasks结果： tf.Tensor([[[[128  64  32  16   8   4   2   1]]]], shape=(1, 1, 1, 8), dtype=uint8)
# # print(bitmasks)
# binchw = tf.reshape(tf.bitwise.bitwise_and(tf.expand_dims(binchwp, axis=3), bitmasks),
#                     [-1, 22, ((19 * 19 + 7) // 8) * 8])
# binchw = binchw[:, :, :19 * 19]
# print("binchw= " ,binchw.shape)
# binhwc = tf.cast(tf.transpose(binchw, [0, 2, 1]), tf.float32)  # 变为 [batch-size,22,361]  ---> [batch-size,361,22]
# # print("binchwc= ",binhwc.shape)
# # print("binchwc= ",binhwc)
# binhwc = tf.math.minimum(binhwc, tf.constant(1.0))  # 取出真正表示棋子的0-1数据
# # print("binchwc= ",binhwc)
# print("binchwc= " ,binhwc.shape)
#
#
# loc = binhwc[1000]
# # print(loc[:,0])
# r  = loc[: ,0:3]
# # print(r[:,0])
# print(r[: ,1])
# print(r[: ,2])
# c= 0
# for i in r[:, 0]:
#     if i != 0:
#         c += 1
# print(c)

# print(binhwc[1001][:,1])

"""

    data["policyTargetsNCMove"] 和 data["binaryInputNCHWPacked"]的解析
    我们假定 黑子为先手，所以在 data["binaryInputNCHWPacked"]的22个特征通道中，第1个通道表示是黑子的位置，第2通道是白子位子 （从第0开始）
    data["policyTargetsNCMove"]是两通道的，总是针对当前执棋者来说，所以并不定说通道0就是黑或者白
    //C0: Policy target this turn. C0：本回合政策目标。 己方策略目标
    //C1: Policy target next turn. C1：下回合政策目标。 对手策略目标
    比如：
    policy_target0 = data["policyTargetsNCMove"][:, 0, :]
    index = np.argmax(policy_target0[1000].numpy()) 
    取出了所有通道0的策略分布，看看第1000个状态的策略落子在哪
    那么就要看ata["binaryInputNCHWPacked"]的第1001个状态矩阵，的binhwc[1001][:,1]和 binhwc[1001][:,2]
    就是看哪个呢？
    若先手是黑子，比如第1000手棋是黑子落的，那么对下一手白子落子，那么白子就成了己方，通道C0的策略就是给白子服务的
    ，在第1001步状态中，应该按照第1000步给出的最大落子概率进行落子，这一步落白子，那么就要看binhwc[1001][:,2]的分布情况
    比较1000给出的落子位置是否和 binhwc[1001][:,2]一致，（看看binhwc[1000][:,2]这一步同样的位置是否落子了，看1001步是否按照策略落子）

    如果符合上面说的，那么就可以构造数据data和标签label的对应关系
    比如 ： binhwc[1001]当前状态局面，那么对应的下一步的预测位置标签是 data["policyTargetsNCMove"][1001, 0, :]所预测的，
    在 binhwc[1002]的binhwc[1000][:,1]展现
    以 binhwc[奇数]的样本，对应样本预测，也就是标签是binhwc[奇数+1][:,1]
    以 binhwc[偶数]的样本，对应样本预测，也就是标签是binhwc[偶数+1][:,2]
    不过为了更清晰，应该配合data["policyTargetsNCMove"]进行one-hot处理

    更好的方法就是直接对data["policyTargetsNCMove"]进行one-hot处理，不用分黑白棋子






"""