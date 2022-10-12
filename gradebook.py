class Gradebook:
    def __init__(self, course, grades):
        self.course = course
        self.grades = grades
        self.school_year = '2022'

    
    def name(self):
        """
        Course name for the gradebook
        """
        course = self.course.lower()

        return f"{course.title()} Gradebook"

    
    def set_school_year(self, year):
        if year > self.school_year:
            self.school_year = year
        
        return self.school_year


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

    
    def letter_grade(self, percentage):
        """
        Return the letter grade based on the grade percentage
        """
        if percentage >= 97:
            return 'A+'
        elif percentage >= 93:
            return 'A'
        elif percentage >= 90:
            return 'A-'
        elif percentage >= 87:
            return 'B+'
        elif percentage >= 83:
            return 'B'
        elif percentage >= 80:
            return 'B-'
        elif percentage >= 77:
            return 'C+'
        elif percentage >= 73:
            return 'C'
        elif percentage >= 70:
            return 'C-'
        elif percentage >= 67:
            return 'D+'
        elif percentage >= 63:
            return 'D'
        elif percentage >= 60:
            return 'D-'
        elif percentage < 60:
            return 'F'