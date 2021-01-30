#31. python program to demonstrate list collection operations

#extend()
"""
l3=[8,9]
l2=[1,2,3,4]
l2.extend(l3)
print(l2)
"""
#output:-[1, 2, 3, 4, 8, 9]

#pop()
"""
l2.pop()
print(l2)
"""
#output:-[1, 2, 3, 4, 8]

#append()
"""
l2.append(1)
print(l2)
"""
#output:-[1, 2, 3, 4, 8, 1]

#remove()
"""
l2.remove(1)
print(l2)
"""
#output:-[2, 3, 4, 8, 1]

#count()
"""
print(l2.count(4))
"""
#output:-1

#append()
"""
l2.append([10,20])
print(l2)
"""
#output:-[2, 3, 4, 8, 1, [10, 20]]

#insert()
"""
l2.insert(4,10)
print(l2)
"""
#output:-[2, 3, 4, 8, 10, 1, [10, 20]]

#extend()
"""
l3=[]
l3.extend([1,2,3,4])
print(l3)
"""
#output:-[1, 2, 3, 4]

#sort()
"""
a=[5,6,1,2,3]
a.sort()
print(a)
"""
#output:-[1, 2, 3, 5, 6]

#reverse()
"""
a.reverse()
print(a)
"""
#output:-[6, 5, 3, 2, 1]

#sum()
"""
print(sum(a))
"""
#output:-17

#max()
"""
print(max(a))
"""
#output:-6

#min()
"""
print(min(a))
"""
#output:-1

#clear()
"""
a.clear()
print(a)
"""
#output:-[]

#copy()
"""
a=[]
b=[1,2,3]
a=b.copy()
print(a)
"""
#output:-[1, 2, 3]

#del
"""
del a[1]
print(a)
"""
#output:-[1, 3]

#len()
"""
print(len(a))
"""
#output:-2

#slice(start:stop:step)
"""
a.extend([5,8,7])
print(a[::])
"""
#output:-[1, 3, 5, 8, 7]

#slice(start:stop:step)
"""
print(a[1:2])
"""
#output:-[3]

#slice(start:stop:step)
"""
print(a[1:4])
print(a[0:4])
"""
#output:-[3, 5, 8]
#[1, 3, 5, 8]

#slice(start:stop:step)
"""
n=[1,2,5]
print(n[:])
print(n[::])
"""
#output:-[1, 2, 5]
#[1, 2, 5]

#slice(start:stop:step)
"""
print(a[0:3:1])
print(a[1:2:1])
"""
#output:-[1, 3, 5]
#[3]

"""
print(a)
print(a[-3])
"""
#output:-[1, 3, 5, 8, 7]
#5

#32. python program to demonstrate Dictionary operations
"""
d={}
print(d)
"""
#output:-{}

"""
d={'id':31134,'name':'surya',1:101}
print(d)
"""
#output:-{'id': 31134, 'name': 'surya', 1: 101}

"""
print(type(d))
"""
#output:-<class 'dict'>

#keys()
"""
print(d.keys())
"""
#output:-dict_keys(['id', 'name', 1])

#values()
"""
print(d.values())
"""
#output:-dict_values([31134, 'surya', 101])

#items()
"""
print(d.items())
"""
#output:-dict_items([('id', 31134), ('name', 'surya'), (1, 101)])

"""
print(d['id'],d['name'],d[1])
"""
#output:-31134 surya 101

#get()
"""
print(d.get('name'))
print(d.get('id'))
"""
#output:-surya
#31134

#copy()
"""
b={}
b=d.copy()
print(b)
"""
#output:-{'id': 31134, 'name': 'surya', 1: 101}

#clear()
"""
b=b.clear()
print(b)
"""
#output:-None

#setDefault(a)
"""
d.setdefault('gender')
print(d)
"""
#output:-{'id': 31134, 'name': 'surya', 1: 101, 'gender': None}

"""
d['gender']="male"
print(d)
"""
#output:-{'id': 31134, 'name': 'surya', 1: 101, 'gender': 'male'}

#update()
"""
d.update(loc="vij")
d.update(lang='telugu')
print(d)
"""
#output:-{'id': 31134, 'name': 'surya', 1: 101, 'gender': 'male', 'loc': 'vij', 'lang': 'telugu'}

"""
d.update(a=1053)
print(d)
"""
#output:-{'id': 31134, 'name': 'surya', 1: 101, 'gender': 'male', 'loc': 'vij', 'lang': 'telugu', 'a': 1053}

"""
d.update(desg='student',hobbies='music')
print(d)
"""
#output:-{'id': 31134, 'name': 'surya', 1: 101, 'gender': 'male', 'loc': 'vij', 'lang': 'telugu', 'a': 1053, 'desg': 'student', 'hobbies': 'music'}

#len()
"""
print(len(d))
"""
#output:-9

"""
d.update({102:546})
print(d)
"""
#output:-{'id': 31134, 'name': 'surya', 1: 101, 'gender': 'male', 'loc': 'vij', 'lang': 'telugu', 'a': 1053, 'desg': 'student', 'hobbies': 'music', 102: 546}

"""
c={}
c.setdefault('gender')
c['gender']="male"
print(c)
"""
#output:-{'gender': 'male'}

"""
c.update([(1,2)])
print(c)
"""
#output:-{'gender': 'male', 1: 2}

"""
c.update(loc="vij",dob='18/11/2001')
print(c)
"""
#output:-{'gender': 'male', 1: 2, 'loc': 'vij', 'dob': '18/11/2001'}

#pop()
"""
c.pop('loc')
print(c)
"""
#output:-{'gender': 'male', 1: 2, 'dob': '18/11/2001'}

#del
"""
del c[1]
print(c)
"""
#output:-{'gender': 'male', 'dob': '18/11/2001'}

"""
print(c.keys())
print(c.values())
"""
#output:-dict_keys(['gender', 'dob'])
#dict_values(['male', '18/11/2001'])
