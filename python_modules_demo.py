"""
import math
print(math.pi)
"""

"""
import math as m
print(m.pi)
"""

"""
from math import pi
print(pi)
"""

"""
from math import pi,e
print(pi)
print(e)
"""

"""
from math import *
print(pi)
print(e)
"""

"""
print(dir())
"""

"""
import os
print(os.name)
os.mkdir("d:\\PFSD")
print(os.getcwd())
os.rmdir("d:\\PFSD")
print(os.listdir())
"""

"""
import datetime
obj=datetime.datetime.now()
print(obj)
d=datetime.date(2021,1,21)
print(d)
"""

"""
from datetime import date
d=date(2021,10,25)
print(d)
"""

"""
from datetime import date
today=date.today()
print("Current date=",today)
"""

"""
from datetime import date
today=date.today()
print(today.year,today.month,today.day)
"""

"""
from datetime import datetime
now=datetime.now()
print(now)

current_time=now.strftime("%H:%M:%S")
print(current_time)
"""

"""
import time
t=time.localtime()
current_time=time.strftime("%H:%M:%S",t)
print(current_time)
"""

"""
import random
print(random.random())

print(random.randint(10,20))

l=[10,20,30,40,50]
print(random.choice(l))

random.shuffle(l)
print(l)

print(random.randrange(1,10))

print(random.randrange(100,1000,3))

print(random.randrange(1000,100,-2))

print(random.choices(l,weights=[5,2,1,6,4],k=3))

print(random.choices(l,k=3))
"""

"""
import math
print(math.factorial(2))

print(math.gcd(5,10))

print(math.pow(3,2))

print(math.isfinite(2/3))

#print(math.isfinite(2/0))

#print(math.isnan("klu"))

print(math.isnan(2))
"""
