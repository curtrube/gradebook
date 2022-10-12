from gradebook import Gradebook

grades = [98, 95, 103]

my_gradebook = Gradebook(course='spanish',grades=grades)

print(my_gradebook.name())
print(f"The high grade is: {my_gradebook.high_grade()}")
print(f"The average grade is: {my_gradebook.average_grade()}")
print(f"The low grade is: {my_gradebook.low_grade()}")
print(f"The letter grade is: {my_gradebook.letter_grade(92)}")
my_gradebook.set_school_year('2020')