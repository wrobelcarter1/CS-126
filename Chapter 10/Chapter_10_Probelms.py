                                                                # Carter Wrobel
                                                                # CS126 - #186
                                                                # 11/30/17
                                                                # Section 1
# Chapter 10 Worksheet Problems


# Problem 1
def test_eq(a,b):
    try:
        assert (a == b)
    except AssertionError:
        print('failed')

test_eq(41,52)
# Assertion Error

#Problem 2
def test_list_eq():
    assert [0,1,2] == [0,1,3]
    print('pass')

test_list_eq()
# Assertion Error

#Problem 3
def test_text():
    assert 'eggs' == 'eggs'
    print('pass')
    
test_text()
# pass

#Problem 4
def test_dict_eq():
    assert {1:0,2:1} == {1:0,2:1}
    print('pass')

test_dict_eq()
# pass

#Problem 5
def test_tuple(a,b):
    assert (a,b) == (1,2)
    print('pass')

test_tuple(1,2)
# pass

#Problem 6
def test_nums():
    assert num1 * 2 < num2
    print('pass')

num1 = 3
num2 = 6
test_nums()
# Assertion Error

#Problem 7
class Cat():
    a = 1
def test_attr():
    i = Cat()
    assert i.a == 2
    print('pass')

test_attr()
# Assertion Error

#Problem 8
class Cat():
    a = 1
    def __init__(self):
        self.a=2

def test_Cat_att():
    i = Cat()
    assert i.a == 2
    print('pass')

test_Cat_att()
# pass

#Problem 9
is_cat = True
is_dog = False
def test_bool():
    assert is_cat or is_dog
    print('pass')

test_bool()
# pass

#Problem 10
def test_in_sentence(x):
    text = 'a cat is not a dog'
    assert x not in text
    print('pass')

test_in_sentence('cats')
# pass

#Problem 11
def test_set_compare(s1,s2):
    s1 = set("1234")
    s2 = set("2345")
    assert s1.issubset(s2)
    print('pass')

s1 = set("1234")
s2 = set("2345")
test_set_compare(s1,s2)
# Assertion Error

#Problem 12
def func():
    return False

def test_func():
    assert func() is False
    print('pass')

test_func()
# pass

#Problem 13
class Animal():
    b = 1

class Bug():
    b = 2

def test_b():
    assert Animal.b == Bug.b
    print('pass')

test_b()
# Assertion Error

#Problem 14
class MyClass:
    def __init__(self, max):
        self.max = max

def test_class():
    c1 = MyClass(20)
    c2 = MyClass(20)
    assert c1 == c2
    print('pass')

test_class()
# Assertion Error

#Problem 15
class Count():
    a = 10
    def __init__(self):
        a = 11

def test_Count():
    c = Count()
    assert c.a == 11
    print('pass')

test_Count()
# Assertion Error

#Problem 16
def test_startswith():
    assert x().startswith(y())
    print('pass')

def x():
    return "0101"

def y():
    return "10"

test_startswith()
# Assertion Error

#Problem 17
def test_expression():
    x = 6*7
    assert x == 42/2*4-42
    print('pass')

test_expression()
# pass

#Problem 18
def test_expression():
    x = 9*3/10+4.3
    assert x > 7
    print('pass')

test_expression()
# Assertion Error

#Problem 19
def test_list():
    alst = [1, 2, 3, 4, 5, 6]
    assert alst[-1] > alst[3]
    print('pass')

test_list()
# pass

#Problem 20
def test_list2():
    alst = [1, [2], [3,4,5],6]
    assert alst[-1] > alst[3]
    print('pass')

test_list2()
# Assertion Error
