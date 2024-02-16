# Assignment 2.1

def find_and_insert_data(friend, k_count) :
    find_pos = -1
    for i in range(len(katok)):
        pair = katok[i]
        if k_count >= pair[1]:
            find_pos = i
            break
    if find_pos == -1:
        find_pos = len(katok)

    insert_data(find_pos, (friend, k_count))


def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)
    k_len = len(katok)

    for i in range(k_len - 1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend


katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]

if __name__ == "__main__":

    while True:
        data = input("추가할 친구--> ")
        count = int(input("카톡 횟수--> "))
        find_and_insert_data(data, count)
        print(f"{katok}\n")
