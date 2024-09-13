a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
def great(a,b,c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    else:
        return c
print(f"Greatest no. between the 3 number is:{great(a,b,c)}")