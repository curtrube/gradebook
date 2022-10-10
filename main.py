from gradebook import Gradebook

grades = []

my_gradebook = Gradebook(grades)

while True:
    grade_input = input("Enter a grade or `q` to quit.\n")

    if grade_input == 'q':
        break

    if grade_input.isdigit():
        grade = int(grade_input)
        grades.append(grade)

    else:
        print("Invalid type detected")



print(f"The high grade is: {my_gradebook.high_grade()}")
print(f"The average grade is: {my_gradebook.average_grade()}")
print(f"The low grade is: {my_gradebook.low_grade()}")
