sum, e, d, e1, e2, e3, e4, d1, d2, d3 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for x in range(1, 10):
    sum = sum + x
    if x % 2 == 0:
        e = e + 1
        if e1 == 0:
            e1 = x
        elif e2 == 0:
            e2 = x
        elif e3 == 0:
            e3 = x
        else:
            e4 = x
    if x % 3 == 0:
        d = d + 1
        if d1 == 0:
            d1 = x
        elif d2 == 0:
            d2 = x
        else:
            d3 = x
print("sum of all numbers is " + str(sum))
print(str(e) + " are even numbers (" + str(e1) + " " + str(e2) + " " + str(e3) + " " + str(e4) + ") , and " + str(d) + " are divisable by 3  (" + str(d1) + " " + str(d2) + " " + str(d3) + ")")
print("program is complete")