'''try:
    doc = open("ade.txt")
    a = doc.read()
    print(a)
    
except IOError as e:
    print("File not exists", e)'''
try:
    doc = 2
    doc1 = "ab"
    #sum = doc + doc1
    ave = doc/0
    print(ave)
    #print(sum)
#except ValueError as e:
    #print("The values cannot be added", e)
    
except ZeroDivisionError as e:
    print("Cannot devide by 0", e)



try:
    for line in readfile("file.txt"):
        print(line.stripe())
