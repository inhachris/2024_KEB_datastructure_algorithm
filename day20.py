class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def print_nodes(start) :
	current = start
	if current is None :
		return
	print(current.data, end=' ')
	while current.link is not None:
		current = current.link
		print(current.data, end=' ')
	print()


def insert_node(find_data, insert_data) :
	global head, current, pre

	if head.data is find_data:      # 첫 번째 노드 삽입
		node = Node()
		node.data = insert_data
		node.link = head
		head = node
		return

	current = head
	while current.link is not None:    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == find_data:
			node = Node()
			node.data = insert_data
			node.link = current
			pre.link = node
			return

	node = Node()                   # 마지막 노드 삽입
	node.data = insert_data
	current.link = node


def delete_node(delete_data) :
	global head, current, pre

	if head.data is delete_data :         # 첫 번째 노드 삭제
		current = head
		head = head.link
		print(f"{delete_data}가 삭제됨")
		del(current)
		return

	current = head                          # 첫 번째  외 노드 삭제
	while current.link is not None :
		pre = current
		current = current.link
		if current.data == delete_data :
			pre.link = current.link
			print(f"{delete_data}가 삭제됨")
			del(current)
			return


def find_node(find_data) :
	global head, current, pre

	current = head
	if current.data is find_data :
		return current
	while current.link is not None :
		current = current.link
		if current.data == find_data :
			return current
	return Node()	# 빈 노드 반환


head, current, pre = None, None, None
data_array = ["다현", "정연", "쯔위", "사나", "지효"]


if __name__ == "__main__" :
    node = Node()		# 첫 번째 노드
    node.data = data_array[0]
    head = node

    for data in data_array[1:] :	# 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node

    print_nodes(head)


    insert_node("다현", "화사")
    print_nodes(head)

    insert_node("사나", "솔라")
    print_nodes(head)

    insert_node("동균", "문별")
    print_nodes(head)

    delete_node("화사")
    print_nodes(head)

    delete_node("쯔위")
    print_nodes(head)

    print(head.data)
    print(find_node("다현").data)
    print(find_node("재남").data)
