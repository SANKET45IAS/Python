iter=["Sanket","Shrijan","Anupam"]

print("With For Loop----")
for i in range(0,len(iter)):
    print(iter[i])

print("With For Loop and Inplace of Range use list name")
for i in iter:
    print(i,end=' ')

print("\n8With While Loop----")
index=0
while(index<len(iter)):
    print(iter[index])
    index+=1