def sum1(a,b):
    x = a+b
    return x


def sum2(*args):
    x = 0
    for i in args:
        x+=i
    return x

def greet(*args):
    for i in args:
       print(i)

def ave2(*args):
    total = 0
    n = 0
    for i in args:
        total+=i
        n+=1
    print(total,n)
    ave1 = total/n
    print(ave1)
    
ave2(2,3,1,4)


def myfu(**kwargs): 
    for key, value in kwargs.items():
        print (key, value)


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
for i in simpleGeneratorFun(): 
    print(i)

#COUNTERS
from collections import Counter
print(Counter(['B','B','A','B','C','A','B','B','A','C']))

import django

  
