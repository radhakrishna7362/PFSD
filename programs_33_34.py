#33. python program to demonstrate tuple operations
"""
t1=(1,2,3)
print(t1)
"""
#output:-(1, 2, 3)

#type()
"""
print(type(t1))
"""
#output:-<class 'tuple'>

#len()
"""
print(len(t1))
"""
#output:-3

#count()
"""
print(t1.count(1))
"""
#output:-1

#index()
"""
print(t1.index(1))
"""
#output:-0

"""
a=(10,20,30,10)
print(a*3)
print(a+t1)
"""
#output:-(10, 20, 30, 10, 10, 20, 30, 10, 10, 20, 30, 10)
#(10, 20, 30, 10, 1, 2, 3)

#list()
"""
b=list(a)
print(b)
"""
#output:-[10, 20, 30, 10]

#sorted()
"""
print(sorted(a))
"""
#output:-[10, 10, 20, 30]

#set()
"""
print(set(a))
"""
#output:-{10, 20, 30}

"""
print(a[-3])
print(a[-2],a[-1])
"""
#output:-20
#30 10

"""
print(a[1:2])
"""
#output:-(20,)

"""
print(a[::-1])
"""
#output:-(10, 30, 20, 10) reverse of a tuple

"""
print(sorted(a))
"""
#output:-[10, 10, 20, 30]

"""
t3[2]="klu"
"""
#output:-we cannot modified in tuple

"""
print(sum(t1),max(t1),min(t1))
"""
#output:-6 3 1

#34. python program to demonstrate set operations

"""
s={}
s1={1,2,3,1}
print(s1)
"""
#output:-{1, 2, 3}

"""
print(len(s1),str(s1),list(s1),type(s1))
"""
#output:-3 '{1, 2, 3}' [1, 2, 3] <class 'set'>

#add()
"""
s1.add(5)
print(s1)
"""
#output:-{1, 2, 3, 5}

"""
s2={3,4,5}
s1.add(6)
s2.add(7)
print(s1,s2)
"""
#output:-{1, 2, 3, 5, 6} {3, 4, 5, 7}

#union()
"""
print(s1.union(s2))
"""
#output:-{1, 2, 3, 4, 5, 6, 7}

#intersection()
"""
print(s1.intersection(s2))
"""
#output:-{3, 5}

#difference()
"""
print(s1.difference(s2))
"""
#output:-{1, 2, 6}

"""
a={1,2,3,4}
b={3,4,5}
a.intersection_update(b)
print(a,b)
"""
#output:-{3, 4} {3, 4, 5}

#difference_update
"""
a={1,2,3,4}
b={3,4,5}
a.difference_update(b)
print(a,b)
"""
#output:-{1, 2} {3, 4, 5}

#empty set
"""
a=set()
print(a)
"""
#output:-set()

"""
a={10,20,30,25}
a.remove(10)
print(a)
"""
#output:-{25, 20, 30}

#discard-it doesn't throw error whether the remove number is not there
"""
a.discard(10)
a.discard(20)
print(a)
"""
#output:-{25, 30}

#update()
"""
a.update({1,2})
print(a)
"""
#output:-{1, 2, 25, 30}

"""
n=set([1,2,3])
print(n)
"""
#output:-{1, 2, 3}

#isdisjoint()-in the two sets there is no common elements returns true else return false
"""
a={1,2,3}
b={1,2,3}
print(a.isdisjoint(b))
b={4,5,6}
print(a.isdisjoint(b))
"""
#output:-False
#True

#pop()-It removes first element in the set
"""
a.pop()
print(a)
"""
#output:-{2, 3}

#symmetric_difference()-it print the not common elements in two sets
"""
a={1,2,3,4,5}
b={3,4,5}
print(a.symmetric_difference(b))
"""
#output:-{1, 2}
