class Student:
    def __init__(self, first_name, last_name, student_id, major):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.major = major

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_student_info(self):
        return f"Студент: {self.get_full_name()}\nID студента: {self.student_id}\nСпеціальність: {self.major}"

student1 = Student("Максім", "Негрович", "54321", "Географія")

print(student1.get_student_info())