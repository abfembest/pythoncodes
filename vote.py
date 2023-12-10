Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> age = [10,20,30,30,40]
>>> if age ==30;
SyntaxError: invalid syntax
>>> if age == 30:
	print(age)

	
>>> age
[10, 20, 30, 30, 40]
>>> for x in age:
	if x>= 30:
		print("Eligible to vote are", x)