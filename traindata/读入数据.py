

import numpy as np
data = np.load('data1.npz')
print(data.files)
print(data["binaryInputNCHWPacked"].shape)
print(data["policyTargetsNCMove"].shape)
# print(data["policyTargetsNCMove"][1][0])

# for i  in data["policyTargetsNCMove"][10][0]:
#     if i !=0:
#         print(i)
print(max(data["policyTargetsNCMove"][10][0]))
# print(data["policyTargetsNCMove"][10][0])
# res = np.where(max(data["policyTargetsNCMove"][10][0]))
# 找到列表里面最大值的下标索引
res = np.where(data["policyTargetsNCMove"][10][0]==max(data["policyTargetsNCMove"][10][0]))
print(data["policyTargetsNCMove"][10][0][279])
print(res)



#  列表最大值索引方法2
#  使用numpy的函数，argmax获得最大元素的索引，相应的获得最小值的话需要使用argmin
arr_aa = np.array(data["policyTargetsNCMove"][10][0])
maxindex  = np.argmax(arr_aa )
minindex  = np.argmin(arr_aa )
print("maxindex=",maxindex)
print("minindex=",minindex)

# 方法3  也可以将numpy转为list，然后使用list或者最大值索引的方法获得最大值。

bb = data["policyTargetsNCMove"][10][0].tolist()
index = bb.index(max(bb))
print("index=",index)

# 可以得到array在全局和每行每列的最大值(最小值同理)
a = np.arange(9).reshape((3,3))
print(np.max(a))        #全局最大
print(np.max(a,axis=0)) #每列最大
print(np.max(a,axis=1)) #每行最大
# 然后用where得到最大值的索引，返回值中，前面的array对应行数，后者对应列数
print(np.where(a == np.max(a))) #表示最大值在第二行第二列
print(np.where(a==np.max(a,axis=0))) # 表示最大值分别在第二行第零列，第二行第一列，第二行第二列