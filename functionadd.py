def sum1():
    val1 = input("Enter value 1: ")
    val2 = input("Enter value 2: ")
    val1 = float(val1)
    val2 = float(val2)
    add = val1 + val2
    #print("The sum of ", val1, "and", val2, "is : ", add)
    return add
    

def power():
    a = sum1()
    #sqr = a**2
    return a**2



def passcode():
    passwd1 = input("Create a password ")
    passwd = input("enter the password ")
    if passwd1==passwd:
        print("Welcome to your dashboard")

    else:
        print("The password your entered is incorect")
    
    
