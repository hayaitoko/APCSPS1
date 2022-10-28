x = -1
sum = 0

while x < 50:
    x = x + 1
    if x == 8:
        print("number is 8")
        continue
    elif (x % 4) == 0:
        sum = sum + x
        print("number is " + str(x) + " and total is " + str(x))
        continue
    else:
        print(str(x) + " is not divisable by 4")
        continue
print("-----------------------------------------------")
print("-----------------------------------------------")
print("program has completed with total of " + str(sum))
print("-----------------------------------------------")
print("-----------------------------------------------")