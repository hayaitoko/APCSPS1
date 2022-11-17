number = [1, 2, 3, 4, 5, 6]
for i in number:
    if i % 2 != 0:
        number.remove(i)
print(number)