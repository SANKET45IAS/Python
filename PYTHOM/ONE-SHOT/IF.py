#Indentation will start from if statement
age=int(input("ENTER AGE :"))
if age >= 18:
    print("YES,YOU CAN VOTE🐚")
elif age<=0 :
    print("Enter valid input")
    age=int(input("ENTER AGE :"))
if age >= 18:
    print("YES,YOU CAN VOTE🐚")
else:
    print("NO,YOU CAN'T VOTE,AFTER",(18-age),"YEAR YOU CAN VOTE")