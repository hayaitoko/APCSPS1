def add(num):
    if (num % 2) == 0:
        return(num * 2)
    else:
        return(num * 3)

x = 0

for i in range(0,5):
    x = x + 1
    print("return value is: " + str(add(x)))