#35.Functions with no arguments and no return values
"""
def add():
    a=10
    b=20
    print(a+b)
add()
"""
#output:-30

#36.Functions with arguments and no return values
"""
def add(a,b):
    
    print(a+b)
add(10,20)
"""
#output:-30

#37.Functions with no arguments and return values
"""
def add():
    a=10
    b=20
    return a+b;
print(add())
"""
#output:-30

#38.Functions with  arguments and return values
"""
def add(a,b):
    
    return a+b;
print(add(10,20))
"""
#output:-30

"""
Types of arguments
1.Required
2.Keyword
3.default
4.variable length
"""

#39.Python Script to demonstrate required arguments
"""
def add(x,y):
    return (x+y)
a=1;b=2
print(add(a,b))
"""
#output:-3

#40.Python Script to demonstrate keyword arguments
"""
def add(x,y):
    return (x+y)

print(add(x=2,y=3))
"""
#output:-5

#41.Python Script to demonstrate default arguments
"""
def add(x,y=3):
    return (x+y)

print(add(2))
print(add(2,6)
"""
#output:-5

#42.Python Script to demonstrate variable length arguments
"""
def sum(*x):
    total=0;
    for n in x:
        total+=n;
    print(total)
    print(x)
sum(10,20,30,40,50)
sum(10,20)
sum(10)
"""
#output:-150
#(10, 20, 30, 40, 50)
#30
#(10, 20)
#10
#(10,)

#43. Python script to find fibinacci of a given number using recursion
"""
def fibinocci(n):
    if n<=1:
        return n
    else:
        return fibinocci(n-1)+fibinocci(n-2)

a=int(input("Enter a number:"))
print(fibinocci(a))
"""

#44. Python script to find factorial of a given number using recursion
"""
def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)

a=int(input("Enter a number:"))
print(factorial(a))
"""

#45. Python script to find sum of n numbers using recursion
"""
def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

a=int(input("Enter a number:"))
print(sum(a))
"""
