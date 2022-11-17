def name():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    x = input("would you like to provide age details?")
    if x == "yes":
        print("your name is: " + fname + " " + lname)
        age()
    else:
        print("thank you")
        print("your name is: " + name + " " + lname)
    
def age():
    uage = input("Enter age: ")
    print("Your age is: " + uage)

x = 0
while x < 1:
    i = input("Will you provide name details?: ")
    if i == "yes":
        x = x + 1
        name()
    else:
        print("try again")