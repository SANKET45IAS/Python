a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=int(input("Enter d:"))
if(a>b and a>c and a>d):
    print("a is greater:",a)
elif(b>a and b>c and b>d):
    print("b is greater:",b)
elif(c>a and c>b and c>d):
    print("c is greater:",c)
else:
    print("d is greater:",d)
