#Same as List but tuple is Immutable we can't change any index value
tup_val=(45,"Sanket",9.45,61)
count=tup_val.count(45)#return the counting value of an element present in the tuple
print("1.Count the occurance of a given value in the tuple:",count)
index=tup_val.index(9.45)#Return the first index value of the searching element in the tuple
print("2.First Index of a Searching element:",index) 

a_tup=(1,2,3,4,5)
h_tup=(6,7,8,9,45)
s_tup=h_tup+a_tup#Concadinate two tuple 
print("3.Join Two Tuple in a Single Tuple",s_tup)
print("4.Return the max number in the Tuple",max(a_tup))#Highest digit value
print("4.Return the min number in the Tuple",min(h_tup))#Lowest digit value
#print(max(tup_val)) Return not supported between instances of 'str' and 'int' error
specify_tup=(1,2,3,2,4,2)
ind=specify_tup.index(2,2,5)#Return the index value between Given Index .index(value,starting Index,ending Index)
print("5.Index of the searching element between given Index:",ind)