math=int(input("Enter Math Marks:"))
physic=int(input("Enter Physics Marks:"))
cs=int(input("Enter Computer Marks:"))
percentage=(100*(math+physic+cs))/300
if(percentage>=34 and math>=35 and physic>=35 and cs>=35):
    print("pass,percentage:",percentage)
else:
    print("fail,percentage:",percentage)
