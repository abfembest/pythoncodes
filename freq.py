a = [2,2,3,4,1, 5,6,7,3,2,4,8,10] 
print("====Frequency Table=====")
print("Number", "\t", "F" , "\t" "FX")
for i in a:
    print(i, "\t", a.count(i), "\t", i*a.count(i))
    if i == i:
    	continue
