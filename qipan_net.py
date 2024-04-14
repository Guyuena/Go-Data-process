import graphviz

dot = graphviz.Digraph(comment='围棋神经网络', format='png')

# 添加节点
dot.node('I1', '输入层', pos='0,0!')
for i in range(19):
    for j in range(19):
        node_name = 'H{}{}'.format(i + 1, j + 1)
        node_label = '({},{})'.format(i, j)
        node_pos = '{},{}!'.format(i + 1, j + 1)
        dot.node(node_name, node_label, pos=node_pos)
dot.node('O1', '输出层', pos='20,0!')

# 添加边
dot.edge('I1', 'H11')
for i in range(19):
    for j in range(19):
        node_name = 'H{}{}'.format(i + 1, j + 1)
        if i > 0:
            dot.edge('H{}{}'.format(i, j + 1), node_name)
        if i < 18:
            dot.edge('H{}{}'.format(i + 2, j + 1), node_name)
        if j > 0:
            dot.edge('H{}{}'.format(i + 1, j), node_name)
        if j < 18:
            dot.edge('H{}{}'.format(i + 1, j + 2), node_name)
        dot.edge(node_name, 'O1')

# 绘制图形
dot.render('go_neural_network', view=True)












