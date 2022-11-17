def name():
    name = input("Enter first name: ")
    lname = input("Enter last name: ")
    print("Your full name is: " + name + " " + lname)

def age():
    age = input("Enter age: ")
    print("your age is: " + age)

x = 0
while x < 1:
    i = input("Do you want age or name details?: ")
    if i == "age":
        age()
        x = x + 1
    elif i == "name":
        name()
        x = x + 1
    else:
        print("Try again")
print("Program done")