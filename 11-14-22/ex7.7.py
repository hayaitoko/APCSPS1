x = 7
def food():
    global x
    x = 3
    print("x2 is: " + str(x))
print("x1 is: " + str(x))
food()
print("x3 is: " + str(x))