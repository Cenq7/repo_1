# Simple School Management System 1

class Student:
    def __init__(self, student_id, name, grade, age):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Age: {self.age}"

class School:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            print("Student with this ID already exists.")
            return
        name = input("Enter Name: ")
        grade = input("Enter Grade: ")
        age = input("Enter Age: ")
        self.students[student_id] = Student(student_id, name, grade, age)
        print("Student added.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted.")
        else:
            print("Student not found.")

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        if student_id in self.students:
            name = input("Enter new Name: ")
            grade = input("Enter new Grade: ")
            age = input("Enter new Age: ")
            self.students[student_id] = Student(student_id, name, grade, age)
            print("Student updated.")
        else:
            print("Student not found.")

    def list_students(self):
        if not self.students:
            print("No students in school.")
        else:
            for student in self.students.values():
                print(student)

    def student_info(self):
        student_id = input("Enter Student ID to search: ")
        if student_id in self.students:
            print(self.students[student_id])
        else:
            print("Student not found.")

def main():
    school = School()
    while True:
        print("\nSchool Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. List All Students")
        print("5. Student Info")
        print("6. Exit")
        choice = input("Select an option (1-6): ")
        if choice == "1":
            school.add_student()
        elif choice == "2":
            school.delete_student()
        elif choice == "3":
            school.update_student()
        elif choice == "4":
            school.list_students()
        elif choice == "5":
            school.student_info()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")

if