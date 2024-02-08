import random

number = random.randint(1,100)
cnt = 0
chance = 7

while(chance != 0):
    a = int(input("Guess the number : "))
    cnt = cnt + 1
    if a < number:
        print("Try bigger\n")
        chance -= 1
    elif a > number:
        print("Try smaller\n")
        chance -= 1
    elif a == number:
        print("You are right!")
        print(f"You tried {cnt} times")
        break

else:
    print(f"You lost. Answer is {number}")