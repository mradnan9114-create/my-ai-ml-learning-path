name = input("enter your name")
marks = int(input("enter your marks"))
if marks > 100 or marks < 0:
    print("invalid marks")
else:
    if marks >= 80:
        print(name,"your grade is A")
        print("excellent")
    elif marks >= 60:
        print(name,"your grade is B")
        print("very good")
    elif marks >= 40:
        print(name,"your grade is C")
        print("good")
    else:
        print(name,"your grade is fail")
if marks >= 40 and marks <= 100:
    print("status:pass")
else:
    print("status:failed")




