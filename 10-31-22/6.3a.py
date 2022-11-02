for x in range(1, 19, 1):
    if x % 2 == 0:
        if x < 10:
            print(str(x))
        else:
            print("number is 2 digit")
    elif x > 9:
        print("number is 2 digit and is not even")
    else:
        print("number is not even")