class Node:
    def __init__(self, number):
        self.number = number
        self.childs = []

    def add_child(self, node):
        self.childs.append(node)

    def get_child(self):
        return self.childs



n = 5
matr = [[0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]]

list_node = [Node(number=i) for i in range(n)]

for i in range(n):
    for j in range(i, n):
        if matr[i][j]==1:
            list_node[i].add_child(list_node[j])
            list_node[j].add_child(list_node[i])

mas = []
mas.append(list_node[0])
visited = [list_node[0]]
ostov = []

while len(mas)!=0:
    current_node = mas.pop()
    for node in current_node.get_child():
        if not node in visited:
            ostov.append([current_node.number, node.number])
            visited.append(node)
            mas.append(node)

print("остов: ", ostov)

