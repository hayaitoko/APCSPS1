#17,18,19,20
#Worksheet
#Write Output? for the following 19 programs (If a program has bugs, fix it)
#Check the answers with Trinket
#1.
def greet(*names):

 
   for name in names:
      print("Hello " +name)
 
greet("Monica","Luke","Steve","John")
#Output??

Hello Monica
Hello Luke
Hello Steve
Hello John


#2.
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Output??
I am from Sweden
I am from India
I am from Norway
I am from Brazil

#3.
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
#Output???

15
25
45

#4.
def calculations(a, b, c=0, d=0):
    return a - b + c - d
print(calculations(12,4))
print(calculations(42,15,d=10))
##Output???

8
17

#5.
def num_return(x,y):
    c = x + y
    return(c)
 
result = num_return(4,5)
print(result)
#Output???

9

#6.
def return_sum(x,y):
    c = x + y
    return c
 
res = return_sum(4,5)
print(res)
#Output??

9

#7.
def calculations(): 
	s = "Perl"
	print(s) 


s = "Python"
calculations()
print(s)
#Output??

Pearl
Python





#8.
def calculations(): 
	global s 
	s = "Perl"
	print(s) 


s = "Python"
calculations()
print(s)
#Output??

Pearl
Pearl

#9
def plus(a, b = 2):
  return a + b
  
print(plus(a=1), 3)
 
print(plus(a=1, b=3))
#Output??

3 3
4

#10
def plus(*args):
  return sum(args)
 
# Calculate the sum
print(plus(1,4,5))
#Output??

10




#11.
def plus(*args):
  total = 0
  for i in args:
    total += i
  return total
print(plus(20,30,40,50))  
#Output?? 

140

#12
def multiply(x,y=0):
                  print("value of x=" + str(x))
                  print("value of y=" + str(y))
    
                  return x*y
  
print(multiply(y=2,x=4))
#Output??

Value of x=4 
Value of y=2
8

#13.
def calculations(s1, s2):
    x = len(s1)
    y = len(s2)
    print(x)
    return x-y
 
z = calculations("Yes","no")
if z > 0:
    print ("First one is longer than second")
else:
    print ("Second one is longer than first one")
#Output??

What is this one trying to do? Check that the word yes is longer than the word no? 

3
First one is longer than second


#14.
def square(x):
     x = 3
     y = x * x
     return y
 
print (square(5) + square(5))
#Output??

18

#15.
def say(message, times = 2):
    print(message * times)
say('Hello')
say('World', 3)
 
#Output??

HelloHello
WorldWorldWorld


#16.
def power(x, y=2):
    r = 1
    for i in range(y):
       r = r * x
    return r
 
print (power(3))
print (power(3, 3))
#Output??

9
27


#17.
def addition(x, y, z): 
   return x + y + z
print((addition(1, 20, 300)))

 #Output??

321

#18.
a =1
b=20
def change():
    global b
    a=45
    b=5
change()
print(a)
print(b)
#Output??

1
5

#19.
def food():
    global total
    total += 1
    return total
total = 0
print(food())
 #Output??

1
