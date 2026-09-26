name = input("enter your name")
marks = int(input("enter your marks"))
attendance = int(input("enter your attendence"))
if marks >100 or marks <0:
    print("invalid marks")
else:
    if attendance >= 75:
        if marks >= 80:
            print(name,"your grade is A")
        elif marks >= 60:
            print(name,"your grade IS B")
        elif marks >= 40:
            print(name,"your grade is C")
        else:
            print(name,"your grade is fail")
    else:
        print("low attendence")
