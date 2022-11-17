mylist = [4, 3, 2, 6, 7, 8]
sum = 0
x = 0
while(x < len(mylist)):
    sum = sum + mylist[x]
    x = x + 1
print(sum) 

sum2 = 0
for i in mylist:
    sum2 = sum2 + i
print(sum2)