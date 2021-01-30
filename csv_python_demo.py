"""
import csv
with open("demo.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    for row in reader:
        print(row[0],",",row[1],",",row[2],",",row[3],",",row[4])
"""

"""
import csv
with open("demo.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    print("****Student Records****")
    next(reader)
    for row in reader:
        print(row[0],",",row[1],",",row[2],",",row[3],",",row[4])
"""

"""
import csv
with open("demo.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    print("****Student Record By Id****")
    next(reader)
    id=int(input("Enter Student Id:"))
    for row in reader:
        if id==int(row[0]):
            print(row[0],",",row[1],",",row[2],",",row[3],",",row[4])
"""

"""
import csv
with open("demo.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
    print("***Student Record By Id & Name")
    id=int(input("Enter Student Id:"))
    name=input("Enter Name:")
    for row in reader:
        if id==int(row[0]) and name==row[1]:
            print(row[0],",",row[1],",",row[2],",",row[3],",",row[4])
"""

"""
import csv
with open("demo.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    print("****Total Salary****")
    next(reader)
    for row in reader:
        totalsal=float(row[3])+float(row[4])
        print(row[0],row[1],totalsal)
"""

"""
import csv
with open("demo1.csv","w",newline="") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["empid","empname","empgender"])
    writer.writerow([1,"covid","female"])
    writer.writerow([2,"klu","male"])
"""

"""
import csv
with open("demo1.csv","a",newline="") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow([3,"ravindra","male"])
    writer.writerow([4,"prasad","male"])
"""

"""
import csv
with open("demo1.csv","r") as csvfile:
    r = csv.reader(csvfile)
    for row in r:
        print(row)
        print(row[0],row[1],row[2])
"""

"""
import csv
with open("demo2.csv","w",newline="") as outputfile:
    writer = csv.writer(outputfile)
    with open("demo1.csv","r") as inputfile:
        reader = csv.reader(inputfile)
        for row in reader:
            writer.writerow(row)
"""
