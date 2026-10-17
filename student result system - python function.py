def calculate_percentage(marks):
percentage = marks / 500 * 100
return percentage

def check_result(percentage):
if percentage >= 40:
return "PASS"
else:
return "FAIL"

student_name = input("Enter student name: ")

marks = int(input("Enter total marks out of 500: "))

percentage = calculate_percentage(marks)

result = check_result(percentage)

print("\n----- STUDENT REPORT -----")
print("Student Name:", student_name)
print("Percentage:", percentage, "%")
print("Result:", result)
