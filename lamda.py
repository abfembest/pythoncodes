def funct(n):
	return lambda a : a + n
add = funct(2)
print (add(5))
        


def lamb(a,b):
    return lambda x,y,z: x+y+z

y = lamb(2, 3)
print(y(2,2,4))



def addval():
    return lambda x: x * 2


d = addval()

def val():
    return lambda k : "Lambda is coming"

dh = val()
print(dh(""))



