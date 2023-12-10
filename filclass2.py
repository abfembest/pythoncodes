import datetime as dt
Fname = "\n My fullname is Abraham O. A."
david = open("dav2.txt","a+")
david.write("Am adding data to my file")
david.write("\n Am adding data on next line to my file ")
x =  dt.datetime.now()
david.write(str(x))
david = open("dav2.txt","a+")
#b = david.read()
#print(b)

for i in david:
    print(i)
