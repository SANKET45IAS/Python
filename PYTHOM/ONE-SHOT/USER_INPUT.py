# input() use for take input from user
name = input("Enter your NAME👨‍💻 - ")
print("YOUR NAME IS -", name)
print(type(name)) #Input take any tyoe of value but return only string value,Output=(<class 'str'>)

#Print 2 Number multiply
#*print("Enter A:")
#a=input()
#print("Enter B:")
#b=input()
#print("A x b =",a*b)
#Output-
#print("A x b =",a*b
#                ~^~
#TypeError: can't multiply sequence by non-int of type 'str' (INT STORED IN STRING CANNOT BE MULTIPLY OR ANY THINK)

#For handle it we use Type casting......
a=int(input("Enter A 📤:"))
b=int(input("Enter B 📤:"))
print("A x b 📥=",a*b)