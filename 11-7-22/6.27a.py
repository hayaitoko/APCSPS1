l1 = []
l2 = []
for x in range(3):
    l1.append(input("Enter data for list 1: "))
for x in range(3):
    l2.append(input("Enter data for list 2: "))
l1.extend(l2)
print(l1)
l1.reverse()
print("after reverse")
print(l1)
print("without element 2")
l1.pop(2)
print(l1)
print("with bob")
l1.insert(2, "bob")
print(l1)
