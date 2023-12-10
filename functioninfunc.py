passwd = input("Enter the password ")
passwd = int(passwd)
passcod = 1234
if passwd == passcod:
    print("welcome")
        
    def sum1():
        val1 = input("Enter value 1: ")
        val2 = input("Enter value 2: ")
        val1 = float(val1)
        val2 = float(val2)
        add = val1 + val2
        print("The sum of ", val1, "and", val2, "is : ", add)
        return add
        

    def power():
        a = sum1()
        sqr = a**2
        print("The square of the numbers is ",sqr)
       
    power()
    

else:
    print("wrong password supplied")
  
