def age():
    uage = int(input("Enter age: "))
    if uage <= 18:
        school()
def school():
    uschool = input("What school do you go to? ")

uname = input("Enter name: ")
if uname == "Bob":
    age()
else:
    print("You're not bob")