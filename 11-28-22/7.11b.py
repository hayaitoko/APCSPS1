list1 = ["Bob", "Andy", "John", "Ben", "Bob"]

def name(inputname):
    print("hello Bob!")
    print("your name is " + inputname)
    global x
    x = x + 1

x = 0
    
for i in list1:
    if i == "Bob" or i == "bob":
        name(i)
    else:
        print("not bob")
print("there are " + str(x) + " Bobs in the list")