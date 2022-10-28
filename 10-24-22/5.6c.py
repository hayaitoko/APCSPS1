for x in range(0, 30):
    if ((x % 2) == 0) and x <= 20:
        print("Value is: " + str(x) + " and it is Winter")
        continue
    elif ((x % 5) == 0) and x <= 20:
        print("Value is: " + str(x) + " and it is Summer")
        continue
    elif (not ((x % 5) == 0) and (not((x % 2) == 0))) and x <= 20:
        print("Value is: " + str(x) + " and it is Spring")
    else:
        print("Valie is: " + str(x) + " and it is Winter/Summer") 
print("progrm is done")