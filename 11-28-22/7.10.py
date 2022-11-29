def list_filler():
    list = []
    listlenght = int(input("how long should the list be?: "))
    for x in range(listlenght):
        y = input("enter list element: ")
        list.append(y)
    return(list)

print(list_filler())