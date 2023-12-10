myfile = open("fil3.txt","a+")

#disp = myfile.read()
#disp1 = myfile.read()
#print(disp)
#for i in myfile:
        #print(i)

#records = "My new records"
#myfile.write("New line addede")
myfile.write("\n I just added a new line of text")
#myfile.write(records)
myfile = open("fil3.txt","a+")
print(myfile.read())
myfile.close()
