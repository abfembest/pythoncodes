import re
from re import split
#p = re.compile("[a-e]")
#a = p.findall("[0-9]")
#print(a)
#print(p.findall("[0-9]"))


"""x = re.compile("[a-e]")
y = x.findall("Bola is a yellow lady.")
print(y)


g = re.compile("Ade")
fname = "Abraham Olufemi Adewale"
print(g.findall(fname))"""

"""d = re.compile("\d")
print(d.findall("I will come by 11 A.M on 10th."))

d = re.compile("\d+")
print(d.findall("I will come by 11 A.M on 10th."))

d = re.compile("\D")
print(d.findall("I will come by 11 A.M 0n 10th."))

d = re.compile("\D+")
print(d.findall("I will come by 11 A.M 0n 10th."))

d = re.compile("\s")
print(d.findall("I will come by 11 A.M 0n 10th."))

d = re.compile("\w+")
print(d.findall("I will come by 11 A.M 0n 10th."))



print(split('\d+', 'On 12th Jan 2016, at 11:02 AM')) 

print(split('\d+', 'On 12th Jan 2016, at 11:02 AM', maxsplit = 1))

                #sub() function or method
print("=====Substaring method in re========")
d = re.sub("o", "*", "God is good and good", count = 0, flags = re.IGNORECASE)
print(d)"""
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)) 

p =  re.subn("o", "*", "Good is god", count = 0, flags = re.IGNORECASE)
print(p)
#To check whether a string starts and ende with thesame character
print("=======To check whether a string starts and ende with thesame character===")
regex  = r"^[a-z]$|^([a-z]).*\1$"
def check(string):
    if(re.search(regex,string)):
        print("Valid")
    else:
        print("Invalid")
        
sample = "abba"
sample2 = "a"
text =  "abcd"


