# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#  数据的预处理，把多余的信息先去除
def train_result_data_process():
    print("start!!!!!!!!")
    total_loss = open("Total_loss.txt","w",encoding="utf-8")
    each_loss  = open("Each_loss.txt","w",encoding="utf-8")
    with open("data.txt", "r", encoding="utf-8") as f_result:
        for line in f_result:  # 读入的每行的数据类型是str  <class 'str'>
            if(line.startswith("INFO:tensorflow:loss =")):
                total_loss.writelines(line)
            elif (line.startswith("INFO:tensorflow:esstloss =")):
                each_loss.writelines(line)
    total_loss.close()
    each_loss.close()
    print("finsh!!!!!")

"""
['INFO:tensorflow:esstloss = 0.11568204',
 ' evstloss = 0.11743326',
 ' fploss = 1.8996396',
 ' gnorm = 205.69951',
 ' leadloss = 0.009422581',
 ' nsamp = 3200',
 ' oloss = 0.917232',
 ' p0loss = 5.6660633',
 ' p1loss = 0.7510473',
 ' pacc1 = 0.0059022233',
 ' pacc10 = 0.0',
 ' pacc4 = 0.0',
 ' pslr = 1e-05',
 ' ptentr = 0.9688468',
 ' rloss = 0.00030486562',
 ' rscloss = 2.5645475e-05',
 ' rsdloss = 2.6012664',
 ' sbcdfloss = 0.46525025',
 ' sbpdfloss = 0.08996354',
 ' skloss = 0.054681085',
 ' skw = 0.048657488',
 ' sloss = 0.78439724',
 ' smloss = 0.0908521',
 ' tdsloss = 0.047601793',
 ' tdvloss = 0.8122532',
 ' vloss = 1.1180632',
 ' vtimeloss = 0.18627131',
 ' wsum = 3200.0 (12.853 sec']
"""

# 根据上面train_result_data_process 处理好的训练结果数据预处理，再根据需要的损失loss进行二次提取
# 只提取特定名字的loss值
def data_process1(input_fname,target_loss):
    save_file_name = target_loss+'.txt'
    target = target_loss+" ="
    file_new =  open(save_file_name, 'w', encoding='utf-8')
    with open(input_fname, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line_new = line[:-1].split(',')
            # print(line_new) # 切片去掉换行符，再以‘，'分割字符串 ，得到一个列表
            # print(line_new)
            for s in line_new:
                s2 = s.strip()
                # print(s2)
                if s2.startswith(target):
                    # print(s2)
                    file_new.writelines(s2+'\n')
            # # print(line_new[3])


# 把每个损失函数的指标名提取出来
def data_process2(input_fname):
    # save_file_name = target_loss+'.txt'
    # file_new = open(input_fname, 'r', encoding='utf-8')
    # line = file_new.read()
    # print(line)
    save_result_name = []
    # 读入文本，读入第一行
    with open(input_fname) as f:
        firstline = f.readline().rstrip()
        print(firstline)
        line_new = firstline[:-1].split(',')
        # print(type(line_new))
        for s in line_new:
            if s.startswith("INFO:tensorflow"):
                s1 = s.replace("INFO:tensorflow:","")
                s2 = s1.split("=")
                print(s2)
                save_result_name.append(s2[0].rstrip())
            else:
                s3 = s.strip()
                s4 = s3.split("=")
                # for ss in s4:
                #     ss2 = ss.replace(" ","")
                #     print(ss2)
                # print(s4[0].rstrip())
                save_result_name.append(s4[0].rstrip())
                # print(type(s4))

    for res in save_result_name:
        print(res)



def list_index_process():
    with open("test.txt", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line_new = line[:-1].split(',')
            # print(type(line_new))
            for s in line_new:
                s2 = s.strip()
                # print(type(s))
                # print(s2)
                if s2.startswith("evstloss ="):
                    print(s2)
            # print(line_new) # 切片去掉换行符，再以‘，'分割字符串 ，得到一个列表



# 批量处理好训练解说stdout.txt的所有数据
def finsh_data_loss_process(input_file):  # 输入训练结果stdout.txt文件即可
    #  数据的预处理，把多余的信息先去除
    print("The Input file is : "+input_file)
    print("start!!!!!!!!")
    total_loss = open("loss_result/loss.txt", "w", encoding="utf-8")
    with open(input_file, "r", encoding="utf-8") as f_result:
        for line in f_result:  # 读入的每行的数据类型是str  <class 'str'>
            line  = line.split(',')
            total_loss.writelines(line[0][16:-1])
            total_loss.writelines('\n')


    total_loss.close()
    #
    # print("processing !!!!!")
    # print("\n")
    #
    # input_file = "./loss_result/Each_loss.txt"
    # save_result_name = []
    # # 读入文本，读入第一行, 先读取一行，获得所有损失函数的指标名字，用来生成指定的TXT文件名
    # with open(input_file) as f:
    #     firstline = f.readline().rstrip()
    #     print(firstline)
    #     line_new = firstline[:-1].split(',') # 字符串转列表
    #     for s in line_new:
    #         if s.startswith("INFO:tensorflow"):
    #             s1 = s.replace("INFO:tensorflow:","")
    #             s2 = s1.split("=")
    #             save_result_name.append(s2[0].rstrip())
    #         else:
    #             s3 = s.strip()
    #             s4 = s3.split("=")
    #             s5 = s4[0].rstrip() # 去除字符串右边一个多余的空格
    #             save_result_name.append(s5)
    #
    # for res in save_result_name:
    #     save_file_name = res + '.txt'
    #     target = res + " ="
    #     file_new = open("./loss_result/"+save_file_name, 'w', encoding='utf-8')
    #     with open(input_file, 'r', encoding='utf-8') as f:
    #         for line in f.readlines():
    #             line_new = line[:-1].split(',') # 切片去掉换行符，再以‘，'分割字符串 ，得到一个列表
    #             for s in line_new:
    #                 s2 = s.strip()
    #                 if s2.startswith(target):
    #                     file_new.writelines(s2 + '\n')
    # print("finsh !!!!!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # train_result_data_process()
    input_file = "loss_result/Total_loss.txt"
    # data_process1(input_file,"leadloss")
    # # list_index_process()
    # data_process2(input_file)
    finsh_data_loss_process(input_file)





