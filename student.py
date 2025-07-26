from data_module import data

class Student:
    def st_login(self, students):
        gr_number = input("Enter Your GR Number: ").strip()
        password = input("Enter Your Password: ")

        try:
            gr_number = int(gr_number)
        except ValueError:
            print("Error: GR Number must be numeric.")
            return False

        for standard_students in students.values():
            for student in standard_students:
                if student.get("gr_number") == gr_number and password == student.get("password").lower():
                    print(f"Welcome {student.get('name')}")
                    self.student_menu(student)
                    return True
        print("Invalid GR Number or Password.")
        return False

    def student_menu(self, student):
        while True:
            choice = input("\n1. View Marks\n2. View Grade\n3. MainMenu\nEnter your choice: ")

            if choice == "1":
                self.view_marks(student)
            elif choice == "2":
                self.view_grade(student)
            elif choice == "3":
                break
            else:
                print("Invalid choice")

    def view_marks(self, student):
        marks = student.get('marks', {})
        if marks:
            for subject, score in marks.items():
                print(f"{subject}: {score}")
        else:
            print("No marks available.")

    def view_grade(self, student):
        marks = student.get('marks', {})
        if marks:
            total = sum(map(int, marks.values()))
            percentage = total / len(marks)
            grade = ("F" if percentage <= 33 else "E" if percentage <= 45 else "D" if percentage <= 60 else "C" if percentage <= 75 else "B" if percentage <= 90 else "A")
            print(f"Total Percentage: {percentage}%")
            print(f"Grade: {grade}")
        else:
            print("No Grade available.")

def student_login():
    student_instance = Student()
    if student_instance.st_login(data.st_name):
        # print("Login successful!")
        pass
    else:
        print("Invalid login credentials.")

if __name__ == "":
    student_login()
