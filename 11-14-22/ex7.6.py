x = 5
def food():
    x = 10
    print("x inside the food function is " + str(x))
print("x outside the food function, beofre food() is " + str(x))
food()
print("x outside the food function after food() is " + str(x))