import random

x = 1
while x == 1:
    user = int(input("enter a number [1-3]: "))
    rnd = random.randint(1, 3)

    if user == rnd:
        print("you win")
        break
    else:
        print("try again")
        continue
print("program end")