a = [ 1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
b = []
y = 0
for x in a:
    if a[y] < 5:
      b.append(a[x])
    y = y +1
print(b)  