l1 = []
l2 = []

for i in range(0,3):
    y = int(input("enter number for list 1: "))
    l1.append(y)
for i in range(0,3):
    y = int(input("enter number for list 2: "))
    l2.append(y)

print(l1)
print(l2)

x = 0
suml1 = 0
while (x < len(l1)):
    suml1 = suml1 + l1[x]
    x = x + 1

x = 0
suml2 = 0
while (x < len(l2)):
    suml2 = suml2 + l2[x]
    x = x + 1

if suml2 > suml1:
    print("list 2 has greater value than list 1")
elif suml1 > suml2:
    print("list 1 has greater value than list 2")
else:
    print("the lists have equal value")