Student_info={
    "name":"Sanket",
    "age":18,
    "Redg_no":9465,
    "course":["WEB DEV","CALCULAS","AD","DL"]
}
print("1.Print whole dictionary ",Student_info)
print("2.Data Type ",type(Student_info))
Student_info["name"]="Sanket Sidhivinayak"
print("3.Modified Dictionary ",Student_info)#Dictionary are mutable we can change the value with the help of the key pair
print("4.",Student_info.items())#Return the list of(Key,value) in tuple form
print("5.Keys in the Dictionary",Student_info.keys())#Return a list containing dictionary keys
print("6.Values in the Dictionary",Student_info.values())#Return a list containing dictionary values
Student_info.update({"age":19,"CGPA":9.45})
print("7.For Update & add ",Student_info)#Return the Update and Add valuesin the Dictionary
print("8.Value of the spceify key ",Student_info.get("name"))#Return the value of the specify key


