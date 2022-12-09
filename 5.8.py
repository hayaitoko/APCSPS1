x = 0
y = 0
while x < 20:
    x = x + 1
    if x % 3 == 0:
        print(str(x) + " is a multiple of 3")
        y = y + x
    elif (x % 3 == 0) and (x % 5 == 0):
        print(str(x) + " is both a multiple of 3 and 5")
        y = y + x
    else:
        print(str(x) + " is not a multiple of 3 or 5")
print("sum of multiples of 3 and 5 is: " + str(y))
    