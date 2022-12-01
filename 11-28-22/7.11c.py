def unnamed(num):
    while num % 2 == 0:
        return(num * 3)
    while num % 2 != 0:
        return(num * 100)
x = int(input("how many times woukd you like to run loop?: "))

for i in range(x):
    print(unnamed(int(input("Enter number: "))))
print("program finished")