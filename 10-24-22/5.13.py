import random

x = random.randint(10, 100)
y = random.randint(10, 100)
z = x + y
print("DEBUG " + str(z))
while x > 1:
    i = int(input("enter your number guess: "))
    if i == z:
        print("you got it!")
        break
    elif i < z:
        print(str(i) + " is less than the number, try again")
        continue
    else:
        print(str(i) + " is above the number, try again")
        continue
print("thanks for playing")