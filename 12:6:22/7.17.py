'''
age height
while loop + functions + defaults

ask if they only have age or height

4 functions ^^
'''

entereddetails = []
count = 0

def age(age = 0):
    print("age is: " + str(age))
    entereddetails.append("Person: " + str(count) + ":")
    entereddetails.append(age)
    
    
def height(height = 0):
    print("height is: " + str(height))
    entereddetails.append("Person: " + str(count) + ":")
    entereddetails.append(height)
    
    
def both(age = 0, height = 0):
    print("height is: " + str(height) + " and age is: " + str(age) + ":")
    entereddetails.append(age)
    entereddetails.append("Person: " + str(count))
    entereddetails.append(height)
    
    
    
    

loopmaster = True

while loopmaster:
    count = count + 1
    detint = input("Do you have age details? height details? both? or neither?: ")
    if detint[0] == "a":
        ageinput = int(input("Please enter age: "))
        age(ageinput)
        loopmaster2 = True
        while loopmaster2:
            listout = input("Would you like to view list of collected data?: ")
            if listout[0] == "y":
                print(entereddetails)
                break
            elif listout[0] == "n":
                loopmaster2 = False
            else:
                print("Error, bad input")
        moreinfo = input("Would you like to enter aditional infromation?: ")
        if moreinfo[0] == "y":
            loopmaster2 = False
        elif moreinfo[0] == "n":
            loopmaster = False
        else:
            print("Error, Bad input")
        
    elif detint[0] == "h":
        heightinput = int(input("Please enter height: "))
        height(heightinput)
        loopmaster2 = True
        while loopmaster2:
            listout = input("Would you like to view list of collected data?: ")
            if listout[0] == "y":
                print(entereddetails)
                break
            elif listout[0] == "n":
                loopmaster2 = False
            else:
                print("Error, bad input")
        moreinfo = input("Would you like to enter aditional infromation?: ")
        if moreinfo[0] == "y":
            loopmaster2 = False
        elif moreinfo[0] == "n":
            loopmaster = False
        else:
            print("Error, Bad input")
    elif detint[0] == "b":
        heightinput = int(input("Please enter height: "))
        ageinput = int(input("Please enter age: "))
        both(ageinput, heightinput)
        loopmaster2 = True
        while loopmaster2:
            listout = input("Would you like to view list of collected data?: ")
            if listout[0] == "y":
                print(entereddetails)
                break
            elif listout[0] == "n":
                loopmaster2 = False
            else:
                print("Error, bad input")
        moreinfo = input("Would you like to enter aditional infromation?: ")
        if moreinfo[0] == "y":
            loopmaster2 = False
        elif moreinfo[0] == "n":
            loopmaster = False
        else:
            print("Error, Bad input")
        
    elif detint[0] == "n":
        loopmaster3 = True
        while loopmaster3:
            repeat = input('Please gather this information and enter "yes" when you are ready to continue, or enter "no" to exit: ')
            if repeat[0] == "y":
                loopmaster3 = False
                break
            elif repeat[0] == "n":
                loopmaster3 = False
                loopmaster = False
                continue
            else:
                print("Error, Bad input")  
    else:
        print("This input is not an option")
        break
