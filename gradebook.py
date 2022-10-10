class Gradebook:
    def __init__(self, grades):
        self.grades = grades


    def average_grade(self):
        """
        Find the average grade from a list of grades.
        """
        average_grade = int(sum(self.grades) / len(self.grades))

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