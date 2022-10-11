class Gradebook:
    def __init__(self, course, grades):
        self.course = course
        self.grades = grades

    
    def name(self):
        course_name = self.course.lower()
        return f"{course_name.title()} Gradebook"


    def average_grade(self):
        """
        Find the average grade from a list of grades.
        """
        average_grade = round(sum(self.grades) / len(self.grades), 1)

        return average_grade


    def high_grade(self):
        """
        Find the high grade from list of grades.
        """
        high_grade = int(max(self.grades))

        return high_grade


    def low_grade(self):
        """
        Find the low grade from a list of grades
        """
        low_grade = int(min(self.grades))

        return low_grade

    
    # def letter_grade(self):
    #     if grade_percentage >= 94: