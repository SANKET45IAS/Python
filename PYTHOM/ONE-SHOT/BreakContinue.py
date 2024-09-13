#Use of break keyword in pythom
for i in range(1,10):
    if i==6:
        break
    print(i)
#Use of continue keyword in pythom
for x in range(1,10):
    if x==5:
        continue
    print(x)
#in while loop it not work
n=1
while n<=10:
    if n==4:
        continue
    print(n)
    n+=1