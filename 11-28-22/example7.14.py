def name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name
x = 0
while (x ==0):
   firstName = input("enter first name: ")
   lastName = input("enter last name: ")
   print(name(firstName, lastName)) 
   x = int(input("enter 0 if you want to continue else 1: "))