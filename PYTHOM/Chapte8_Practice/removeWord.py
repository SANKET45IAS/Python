def rem(l,word):
        n=[]
        for item in l:
            if(not(item==word)):
                n.append(item.strip(word))
        return n
l=["SANKET","SHRIJAN","JAGAN","ARPIT","KUMAR"]
n=input("Enter name:")
print(rem(l,n))