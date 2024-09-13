def sumn(n):
    if(n==1):
        return 1
    return n+sumn(n-1)
n=int(input("Enter a no. :"))
print(f"Sum till {n} natural number is:{sumn(n)}")
