#1 Hello world
"""
print('Hello KLU')
"""
#2 Single and multiple variables
"""
a=10
print(a)
a,b=2,5
print(a+""+b)
"""
#3 type() 
"""
a=5
b=6.3
c='sai'
print(type(a))
print(type(b))
print(type(c))
"""
#4 type conversions
"""
print(int(15.4))
"""
#5 arthematic operators
"""
a=int(input('Enter 1st value'))
b=int(input('Enter 2nd value'))
print("Sum:",a+b)
print("Diff:",a-b)
print("mul:",a*b)
print("div:",a/b)
print("mod:",a%b)
"""
#6 given number is +ve or not if it -ve convert it into +ve
"""
a=int(input("Enter the value"))
if a<0:
    a=-a
print("Value: ",a)
"""
#7 check the given number is even or odd
"""
a=int(input("Enter the value: "))
if a%2==0:
    print(a,"is an even number")
else:
    print(a,"is an odd number")
"""
#8 display the largest number among 2 numbers
"""
a=int(input("Enter the value: "))
b=int(input("Enter the value: "))
if(a>b):
    print(a,"is the largest number")
else:
    print(b,"is the largest number")
"""
#9 display the largest number among 3 numbers using nested if
"""
a=int(input("Enter the value: "))
b=int(input("Enter the value: "))
c=int(input("Enter the value: "))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
"""
#10.python script to display largest number among three numbers using else if ladder(elif)
"""
a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
c=int(input("Enter third value:"))
if(a>b and a>c):
    print(a,"is big")
elif(b>c):
    print(b,"is big")
else:
    print(c,"is big")
output:-
Enter first value:50
Enter second value:20
Enter third value:30
50 is big
"""
#11.python script to check whether a citizen is elgible for voting or not
"""
n=int(input("enter your age:"))
name=input("enter your name:")
if(n>=19):
    print(name," is eligible")
else:
    print(name," is not eligible")
output:-
enter your age:25
enter your name:pavan
pavan  is eligible
"""
#12.program to print 1 to n natural numbers using for loop
"""n=int(input("enter range"))
for i in range(1,n+1):
    print(i)
output:-
enter range5
1
2
3
4
5"""
#13.Program to print even numbers for a given range using for loop
"""
n=int(input("enter range"))
for i in range(0,n+1):
    if(i%2==0):
        print(i)
output:-
enter range23
0
2
4
6
8
10
12
14
16
18
20
22
"""
#14.Program to print even numbers for a given range using for loop
"""
n=int(input("enter range"))
for i in range(1,n+1):
    if(i%2!=0):
        print(i)
output:-
enter range25
1
3
5
7
9
11
13
15
17
19
21
23
25

"""
#15.Program to print a message "Advance Happy new Year 2021" When a number is divisible by 3 otherwise print the value for the giving
#range of numbers
"""
n=int(input("Enter range:"))
for i in range(1,n+1):
    if(i%3==0):
        print("Advance Happy new Year 2021");
    else:
        print(i);
output:-
Enter range:25
1
2
Advance Happy new Year 2021
4
5
Advance Happy new Year 2021
7
8
Advance Happy new Year 2021
10
11
Advance Happy new Year 2021
13
14
Advance Happy new Year 2021
16
17
Advance Happy new Year 2021
19
20
Advance Happy new Year 2021
22
23
Advance Happy new Year 2021
25
"""
#16.program to print 1 to n natural numbers using while loop
"""n=int(input("enter range:"))
i=1
while(i<=n):
    print(i)
    i+=1
In this loop there is no operator(++ or --)
output:-
enter range:20
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

"""
#17.program to print 1 to n natural numbers using while loop
"""
n=int(input("enter range"))
i=1
while(True):
   print(i)
   i+=1
   if(i>n):
       break
output:-
enter range5
1
2
3
4
5
"""
#18.program to print individual characters from the given string using for loop
"""
name=input("enter string")
for ch in name:
    print(ch);
output:-
"""
#19.program to demonstrate break statement.
"""
n=int(input("enter range"))
for i in range(1,n+1):
    if(i==5):
        break
    else:
        print(i)
output:enter range5
1
2
3
4
"""
#20.program to demonstrate continue statement.
"""
n=int(input("enter range"))
for i in range(1,n+1):
    if(i==7):
        continue
    else:
        print(i)
output:-
enter range:10
1
2
3
4
5
6
8
9
10
"""
#21.program to demonstrate pass statement.
"""
n=int(input("enter range"))
for i in range(1,n+1):
    if(i==7):
        pass
    print(i)
out:enter range10
1
2
3
4
5
6
7
8
9
10
"""
#22.program to demonstrate continue and pass statement
"""
name=input("enter name:");
for i in name:
    if(i=='s'):
        print("pass statement here");
        pass
    print(i)
output:-enter name:surya
pass statement here
s
u
r
y
a
name=input("enter name:");
for i in name:
    if(i=='s'):
        print("pass statement here");
        continue
    print(i)
output:-enter name:surya
continue statement here
u
r
y
a
"""
#23.program to demonstrate for loop with else statement
"""
n=int(input("Enter range:"))
for i in range(1,n+1):
    if(i%2==0):
        print(i)
else:
    print("end of for loop");
output:Enter range:10
2
4
6
8
10
end of for loop
output:Enter range:0
end of for loop
"""
#23.program to demonstrate while loop with else statement
"""n=int(input("Enter range:"))
i=1
while(i<=n):
    print(i)
    i+=1
else:
    print("end of while loop")
output:-
Enter range:5
1
2
3
4
5
end of while loop"""
#25. Program to check whether given number is prime number or not
"""
n=int(input("Enter a value "))
if n > 1:
   for i in range(2,n):
       if (n % i) == 0:
           print(n,"is not a prime number")
           break
   else:
       print(n,"is a prime number")
"""
#26. Program to check whether given number is armstrong number or not
"""
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
"""
#27. Program to check whether given number is palindrome or not
"""
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

"""
#28. Program to print factors of a given number

"""
n=int(input("Enter a value: "))
i = 1
while i <= n : 
    if (n % i==0) : 
        print(i)
    i = i + 1
"""

#29. Program to print divisors of a given number
"""
n=int(input("Enter a value: "))
for i in range(1, int(n/2)+1):
       if n % i == 0:
           print(i)
"""

#30. Program to print prime numbers for a given range
"""
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)
"""
