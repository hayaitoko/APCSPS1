x = 0
inplist = []
while x < 5:
    y = int(input("input a number 1-5 : "))
    if (y > 0) and (y < 6):
        inplist.append(y)
        x = x + 1
    else:
        print("number not 1-5, try again")
print(inplist)
sum = 0
z = 0
while (z < len(inplist)):
    sum = sum + inplist[z]
    z = z + 1
print("sum of numbers is: " + str(sum))