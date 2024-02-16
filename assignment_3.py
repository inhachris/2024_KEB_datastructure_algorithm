# Assignment 3.1

class Node():
    def __init__ (self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current is None:
        return
    print(current.data, end=' ')
    while current.link is not None:
        current = current.link
        print(current.data, end=' ')
    print()

def make_simple_linked_list(nameEmail):
    global head, current, pre

    node = Node()
    node.data = nameEmail
    if head is None:
        head = node
        return

    if head.data[1] > nameEmail[1]:
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data[1] > nameEmail[1]:
            pre.link = node
            node.link = current
            return

    current.link = node

head, current, pre = None, None, None

if __name__ == "__main__":
    while True:
        name = input("이름--> ")
        if name == "":
            print("프로그램을 종료합니다.")
            break
        email = input("이메일--> ")
        make_simple_linked_list([name, email])
        print_nodes(head)
        print("")
