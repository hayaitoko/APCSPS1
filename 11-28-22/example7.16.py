def listfunction(names):
    for x in names:
        if len(names)==3:
            return names[1]

names = ["Bob", "Andy", "John"]
print(listfunction(names))