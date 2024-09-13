#List are the container to store a set's of value of any type of data
leest=["Sanket",45,"G1",True,9.45]
leest[2]="2G1"#1. To change the Indexing Value
print("1.After Change the value of an index",leest)
leest.append("ITER")#2. Insert value at the last of the list
print("2.Insert value at the last index  of the list ",leest)
leest.insert(2,"2ND YEAR")#3. Insert value at the given Index insert(index,value)
print("3.Insert value at given index of the list",leest)
pop_val=leest.pop(3)#4. Revome the index value
print("4.Remove the index value in the list:",leest,"Value:",pop_val)

num=[2,5,3,4,6,9,45,97,18,21]
num.sort()#Arranging in Accending Order
print("5.Sorted in the Accending Order",num)
num.reverse()#Reverse the list
print("6.Reverse the list ",num)
rem_val=num.remove(2)#Remove the given value if it is in the list
print("7.Remove the given number if it's in the list ",num,"Remove Value:",rem_val)
print("8.Indexing value ",num[0:])
num.clear()#Make the list empty
print("9.Use to make Empty the List",num)