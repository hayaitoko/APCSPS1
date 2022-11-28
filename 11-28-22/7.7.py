def product(num1, num2):
    x = num1 * num2
    print(str(num1) + " * " + str(num2) + " = " + str(x))

def addition(num1 , num2):
    x = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(x))
    
while True:
    y = int(input("enter the first number: "))
    z = int(input("enter the second number: "))
    if y == z:
        product(y, z)
    else:
        addition(y, z)
    e = input("Would you like to continue? ")
    if e[0] != "c":
        break
    
print("thank you!")