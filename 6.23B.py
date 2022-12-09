numbers = [ 1,4,7,2,5,9,34,2,96,64,78,3,6]

y = 0
for x in numbers:
    y = y + 1
    if y == 9:
        break
    else:
        if x % 2 == 0:
            print(str(x))
print("Number is 96")