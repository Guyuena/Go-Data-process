import tkinter  # 导入tkinter模块

from data_line.result_line import drawing
items = []  # 初始化选项列表

root = tkinter.Tk()  # 创建窗口
root.title('普通代码程序')  # 设置标题
root.geometry('500x300')  # 设置窗口大小为500x300
root.resizable(width=True, height=True)  # 禁止修改窗口大小


def choose_a():
    items.append('A')
    drawing("oloss")
def choose_b():
    drawing("p0loss")
def choose_c():
    drawing("p1loss")
def choose_d():
    drawing("pacc1")
def choose_e():
    drawing("pacc4")
def choose_f():
    drawing("vloss")

tkinter.Button(root, text='oloss',  font=('软体雅黑', 15),command=choose_a, bd=10,height=True,fg='red').pack()  # root参数的完整形式是master=root
tkinter.Button(root, text='p0loss', font=('软体雅黑', 15),command=choose_b, bd=10,height=True,fg='red' ).pack()
tkinter.Button(root, text='p1loss', font=('软体雅黑', 15),command=choose_c, bd=10,height=True,fg='red' ).pack()
tkinter.Button(root, text='pacc1',  font=('软体雅黑', 15),command=choose_d, bd=10,height=True,fg='red' ).pack()  # 更多选项以此类推
tkinter.Button(root, text='pacc4',  font=('软体雅黑', 15),command=choose_e, bd=10,height=True,fg='red' ).pack()  # root参数的完整形式是master=root
tkinter.Button(root, text='vloss',  font=('软体雅黑', 15),command=choose_f, bd=10,height=True,fg='red' ).pack()


# def show():
#     '''输出已选择的选项列表'''
#     print(items)
#
#
# tkinter.Button(master=root, text='输出已选选项', command=show).pack()

root.mainloop()  # 窗口持久化
