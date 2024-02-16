# Assignment 4.2

class Node():
    def __init__(self):
        self.data = None
        self.r_link = None
        self.l_link = None

head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":

    node = Node()
    node.data = data_array[0]
    head = node

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data

        pre.r_link = node
        node.l_link = pre

    current = head
    print(f"정방향 --> {current.data}", end = ' ')
    while current.r_link is not None:
        current = current.r_link
        print(current.data, end = ' ')

    print()

    print(f"역방향 --> {current.data}", end=' ')
    while current.l_link is not None:
        current = current.l_link
        print(current.data, end=' ')