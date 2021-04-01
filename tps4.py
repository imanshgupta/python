class Student:
    def _init_(self):

        self.name = input("Enter your name")
        self.marks_list = []
        for subject in range(5):
            self.marks_list.append(int(input("Enter marks for subject")))

    def calculate_grade(self):
        self.total_marks = 0
        self.grade = ""
        for score in self.marks_list_tuple:
            self.total_marks += score
        average = self.total_marks / len(self.marks_list_tuple)
        if average >= 90:
            self.grade = "S"
        elif average >= 80:
            self.grade = "A"
        elif average >= 70:
            self.grade = "B"
        return (f"{self.name} got {average} marks on average.\n and a grade of {self.grade}")


n = int(input("Enter number of students"))
students = [Student() for x in range(n)]


filename = input("Enter filename: ")
with open(filename, 'a') as file1:
    for student in students:

        file1.write(str(student.marks_list) + "\n")
        file1.write(student.calculate_grade() + "\n")
        file1.write(f"{student.name} scored a total marks of " +
                    str(student.total_marks) + "\n")
        print("Student data saved")
