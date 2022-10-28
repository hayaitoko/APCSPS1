x = 0
pnum = 0
while x <= 5:
    pnum = pnum + 1
    inpt = int(input("enter player " + str(pnum) + "'s age: "))
    if inpt == 15:
        print("player number " + str(pnum)  + " has made the team")
        x = x + 1
        continue
    elif inpt < 15:
        print("player is too young")
        continue
    else:
        print("player is too old")
        continue
print("team positions are filled")