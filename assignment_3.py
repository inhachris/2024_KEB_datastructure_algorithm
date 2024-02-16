# Assignment 3.2

import random

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_nodes(start):
    current = start
    if current is None:
        return
    print(current.data, end = ' ')
    while current.link is not None:
        current = current.link
        print(current.data, end = ' ')
    print()

def make_simple_linked_list(lotto):
    global head, current, pre

    node = Node()
    node.data = lotto
    if head is None:
        head = node
        return

    if head.data > lotto:
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data > lotto:
            pre.link = node
            node.link = current
            return

    current.link = node

head, current, pre = None, None, None

def find_node(lotto):
    global head, current, pre

    if head is None:
        return False
    current = head
    if current.data is lotto:
        return True
    while current.link is not None:
        current = current.link
        if current.data is lotto:
            return True
    return False

if __name__ == "__main__":
    # lotto_number = []
    i = 1
    while i < 7:
        lotto_number = random.randint(1, 45)
        if find_node(lotto_number):
            continue
        make_simple_linked_list(lotto_number)
        i += 1

    print_nodes(head)