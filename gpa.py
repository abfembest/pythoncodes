print("======CGPA CALCULATOR====")
n = int(input("How many courses? "))
crs = []
units = []
scor = []
point = []
points = []
point2 = 0
eu=0
for i in range(1,n+1):
    a = input("Enter course: ")
    crs.append(a)
    unit = int(input("How many units?: "))
    units.append(unit)
    scr = int(input("Your Score?: "))
    scor.append(scr)
    i+=1
#print("Cousre code","\t", "Units", "\t", "Scores")    
print(crs)
print(units)
print(scor)
    
for i in scor:
    if i >=70:
        point.append(5)
    elif i<70 and i>=60:
        point.append(4)
    elif i<60 and i >=50:
        point.append(3)
    elif i<50 and i>=45:
         point.append(2)
    elif i<45 and i>=40:
         point.append(1)
    else:
         point.append(0)
print(point)
for x,y in zip(units, point):
        points.append(x*y)
print(points)

for a in points:
    point2+=a
print(point2)
for b in units:
    eu+=b
print(eu)
gpa=point2/eu
print(gpa)
if gpa >=4.5:
    print("first class")
elif gpa <4.5 and gpa >=3.5:
    print("second class upper")
elif gpa <3.5 and gpa >=2.5:
    print("second class lower")
elif gpa <2.5 and gpa >=1.5:
    print("third class ")
else:
    print("pass")


    

    
        

    
    
