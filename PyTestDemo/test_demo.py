import demo
import pytest
import mysql.connector
"""
#@pytest.mark.skip(reason="I don't like test_demo")
#@pytest.mark.number
def test_add():
    assert demo.add(7,3) == 10
    assert demo.add(7) == 9
    assert demo.add(5) == 7

#@pytest.mark.number
def test_product():
    assert demo.product(5,5) == 25
    assert demo.product(5) == 10
    assert demo.product(7) == 14

#@pytest.mark.string
def test_add_strings():
    result=demo.add("PFSD","-CC")
    assert result=="PFSD-CC"
    assert type(result) is str
    assert "PFSD" in result
    assert "EP" not in result

#@pytest.mark.string
def product_strings():
    assert demo.product("PFSD ",3)== "PFSD PFSD PFSD"
    result=demo.product("PFSD ")
    assert result=="PFSD PFSD"
    assert  type(result) is str
    assert "PFSD" in result
    assert "EP" not in result
"""

"""
@pytest.mark.parametrize('num1,num2,result',[
    (7,3,10), #first tuple
    ('PFSD','-CC','PFSD-CC'), #second tuple
    (10.5,25.5,36) #third tuple
])

def test_add(num1,num2,result):
    assert demo.add(num1,num2) == result
"""

"""
@pytest.fixture()
def setup():
     print("Once Before Every Method")
def testmethod1(setup):
     print("This is Test Method 1")
def testmethod2(setup):
     print("This is Test Method 2")
"""

"""
import pytest
@pytest.yield_fixture()
def setup():
    print("Once Before Every Method")
    yield
    print("Once After Every Method")

def testmethod1(setup):
    print("This is Test Method 1")

def testmethod2(setup):
    print("This is Test Method 2")
"""

db_connection=mysql.connector.connect(host="localhost",port="3306",user="root",passwd="190031187",database="pfsd")
print("Database connected!!")
cursor=db_connection.cursor()

@pytest.mark.insertrecord #insertrecord - marker
def test_insert_record():
    try:
        cursor.execute("insert into emp values(3,'rk','male')")
        db_connection.commit();
        assert cursor.rowcount==1
    except:
        print("Exception Occured")
    else:
        print("No Exception")

@pytest.mark.viewrecord
def test_view_record():
    cursor.execute("select id from emp where name='klef'")
    for row in cursor:
        assert row[0]==2
