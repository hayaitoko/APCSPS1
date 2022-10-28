frenz = 0
total = 0

while frenz <= 9:
    frenz = frenz + 1
    if frenz % 2 == 0:
        total = total + frenz
        print("your number is " + str(frenz) + " and you will get " + str(frenz) + " candies")
        print("bringing the total candies to " + str(total))
        continue
    else:
        print("your number is " + str(frenz) + " meaning you wont get candy")
        print("keping the total at " + str(total))
        continue
print("program is complete")