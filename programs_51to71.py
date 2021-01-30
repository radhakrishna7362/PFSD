#51. Python program to demonstrate class and object
"""
class Employee:
    id=4654
    name="KLU"
    def display(e):
        print("Employee Id:",e.id,"Employee Name:",e.name)
emp=Employee()
emp.display()
"""
#52. Python program to demonstrate class and object using __init__ method
"""
class Employee:
    def __init__(e,id,name):
        e.id=id
        e.name=name
    def display(e):
        print("Employee Id:",e.id,"Employee Name:",e.name)
emp=Employee(101,"KLU")
emp.display()
"""
#53. Python program to demonstrate non parameterized constructor
"""
class Employee:
    def __init__(e):
        print("Non parameterized constructor")
emp=Employee()
"""
#54. Python program to demonstrate parameterized constructor
"""
class Employee:
    def __init__(e,id,name):
        print("Parameterized Constructor")
        print("Employee Id:",id,"Employee Name:",name)
emp=Employee(19,"COVID")
"""
#55. Python program to demonstrate single inheritance
"""
class A:
    def view(a):
        print("Class A Method")
class B(A):
    def display(b):
        print("Class B Method")
obj1=A()
obj1.view()
obj2=B()
obj2.display()
obj2.view()
"""
#56. Python program to demonstrate multi level inheritance
"""
class A:
    def display1(a):
        print("Class A Method")
class B(A):
    def display2(b):
        print("Class B Method")
class C(B):
    def display3(c):
        print("Class C Method")
obj1=A()
obj2=B()
obj3=C()
obj1.display1()
obj2.display2()
obj3.display3()
obj2.display1()
obj3.display2()
obj3.display1()
"""
#57. Python program to demonstrate multiple inheritance
"""
class A:
    def display1(a):
        print("Class A Method")
class B():
    def display2(b):
        print("Class B Method")
class C(A,B):
    def display3(c):
        print("Class C Method")
obj1=A()
obj2=B()
obj3=C()
obj1.display1()
obj2.display2()
obj3.display3()
obj3.display2()
obj3.display1()
"""
#58. Python program to demonstrate hierarichal inheritance
"""
class A:
    def display1(a):
        print("Class A Method")
class B(A):
    def display2(b):
        print("Class B Method")
class C(A):
    def display3(c):
        print("Class C Method")
obj1=A()
obj2=B()
obj3=C()
obj1.display1()
obj2.display2()
obj3.display3()
obj2.display1()
obj3.display1()
"""
#59. Python program to demonstrate hybrid inheritance
"""
class A:
    def display1(a):
        print("Class A Method")
class B(A):
    def display2(b):
        print("Class B Method")
class C(B):
    def display3(c):
        print("Class C Method")
class D(B,A):
    def display4(d):
        print("Class D Method")
obj1=A()
obj2=B()
obj3=C()
obj4=D()
obj1.display1()
obj2.display2()
obj3.display3()
obj4.display4()

obj2.display1()
obj3.display2()
obj3.display1()
obj4.display2()
obj4.display1()
"""
#60. Python program to demonstrate Polymorphism (Method Overloading)
"""
class Shape:
    def area(s,a=None,b=None):
        if a!=None and b!=None:
            print("Area:",a*b)
        elif a!=None:
            print("Area:",a*a)
        else:
            print("Area:",0)
s=Shape()
s.area()
s.area(5)
s.area(5,10)
"""
#61. Python program to demonstrate Method Overriding
"""
class A:
    def display(a):
        print("Class A Method")
class B(A):
    def display(b):
        print("Class B Method")
obj1=A()
obj2=B()
obj1.display()
obj2.display()
"""

#62.Python program to count number of instances created
"""
class Student:
    count=0
    def __init__(s,name,age):
        s.name=name
        s.age=age
        Student.count+=1
    def display(s):
        print("Name:",s.name,"Age:",s.age)
obj1=Student("KLU",40)
obj2=Student("KLEF",20)
obj3=Student("COVID",2)
obj1.display()
obj2.display()
obj3.display()
print("Total Number Of Objects Created:",Student.count)
"""
#63. Python program to demonstrate super() method
"""
class College:
    def __init__(self,id,cname,location):
        self.id=id
        self.cname=cname
        self.location=location
class Department(College):
    def __init__(self,id,cname,location,dname):
        super().__init__(id,cname,location)
        self.dname=dname
cse=Department(101,"KLU","VJA","CSE")
print(cse.id,cse.cname,cse.location,cse.dname)
"""
#64. Python program to demonstrate exception handling-1
"""
try:
    a=int(input("Enter first value:"))
    b=int(input("Enter second value:"))
    print(a/b)
except:
    print("Divisible by zero exception")
"""
#65. Python program to demonstrate exception handling-2
"""
try:
    l=[10,20,30]
    print(l[4])
except:
    print("Exception Occured")
else:
    print("No Exception Raised")
"""
#66. Python program to demonstrate exception handling-3
"""
try:
    #x="siva"
    print(x)
except NameError:
    print("Variable not found")
else:
    print("No Exception raised")
"""
#67. Python program to demonstrate exception handling-4
"""
try:
    l=[10,20,30,40,50]
    #print(l[2])
    print(l[7])
except IndexError:
    print("IndexOutOfException")
else:
    print("No Exception Occured")
"""
#68. Python program to demonstrate multiple exception
"""
try:
    l=[10,20,30,40,50]
    #print(l[5])
    #print(10/20)
    print(1/0)
except IndexError:
    print("IndexOutOfException")
except ZeroDivisionError:
    print("Divided by zero error")
else:
    print("No Exception Occured")
"""
#69. Python program to demonstrate finally keyword
"""
try:
    l=[10,20,30,40,50]
    print(l[6])
except IndexError:
    print("IndexOutOfException")
finally:
    print("End of program")
"""
#70. Python program to demonstrate raise block
"""
try:
    raise IndexError
except IndexError:
    print("IndexOutOfException")
except ZeroDivisionError:
    print("Divided by zero error")
else:
    print("No Exception Occured")
"""
#71. Python program to demonstrate custom except/User defined exception
"""
n = int(input("Enter number:"))
if n<0:
    raise Exception("Raised an exception")
else:
    print("No Exception occured")
"""
