sum = 0
for x in range(1, 11):
    if x % 2 == 0:
        print(str(x) + " is even")
        continue
    else:
        sum = sum + x
        print(str(x) + " is odd, total is " + str(sum))
        continue
print("program has finished, total is " + str(sum))