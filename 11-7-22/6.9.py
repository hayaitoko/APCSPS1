s = input("enter a string: ")
y = 0
for x in s:
    if x == 'd':
        y = y + 1
print("there are " + str(y) + " ds in the string")