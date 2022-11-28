def city(name, people):
    print("For city " + name + " pop is: " + str(people))
 
while True:
    z = input("Enter city name: ")
    a = int(input("enter city population: "))
    city(z, a)
    l = input("Would you like to exit or continue? ")
    if l[0] != "c":
        break
    
print("thank you! ")