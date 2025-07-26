from data_module import data

class admin_module:
    @staticmethod
    def admin_login():
        user_name = "admin"
        user_password = "admin123"
    
        user = input("Enter Your AdminName: ")
        password = input("Enter Your Password: ")

        if user == user_name and password == user_password:
            print(f"Welcome {user}")
            return True 
        else:
            print("Your data is wrong")
            return False  

    @staticmethod
    def selection(standard,subject, st_name, st_subject):
        while True:
            print("\n1. Manage Students")
            print("2. Student Marks")
            print("3. View Percentage and Grade")
            print("4. Login Page")
            choice = input("Enter your choice (1 to 4): ")

            if choice == "1":
                admin_module.manage_students(standard,subject, st_name)
            elif choice == "2":
                admin_module.student_marks_manage(standard, st_subject, st_name)
            elif choice == "3":
                admin_module.student_percentage_grade(standard,st_name)
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Select a correct number.")

    def manage_students(standard, subject, st_name):

            while True:
                print("\n1.Add Student ")
                print("2.Update Student ")
                print("3.Delete Student ")
                print("4.View Student ")
                print("5.MainMenu ")
                choice=input("Enter your choice for student (1 to 5): ")

                if choice == "1":
                    while True:
                        try:
                            standard = int(input("Enter the standard (1 to 10): "))
                            if 1 <= standard <= 10:
                                print(f"Your standard is: {standard}")
                                break  
                            else:
                                print("Enter a valid standard between 1 and 10.")
                        except ValueError:
                            print("Please enter a valid number.")

                    new_student_name = input("Enter your name: ")

                    if standard not in st_name:
                        st_name[standard] = []  

                    if st_name[standard]:  
                        max_roll_number = max(student.get("roll_number", 0) for student in st_name[standard])
                        max_gr_number = max(student.get("gr_number", 0) for student in st_name[standard])
                    else:
                        max_roll_number = 0  
                        max_gr_number=0

                    new_student = {
                        "name": new_student_name,
                        "roll_number": max_roll_number + 1 ,
                        "gr_number": max_gr_number + 1,
                        "password": f"{max_gr_number + 1}@{new_student_name.split()[0]}"
                    }

                    st_name[standard].append(new_student)
                    print(f"{new_student} added to standard {standard}.")
                    found=True

                    if not found:
                        print("Student not found.")
                    else:
                        print(f"\nUpdated list of students in standard {standard}:")
                        for student in st_name[standard]:
                            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Gr Number: {student['gr_number']}, Password: {student['password']}")


                elif choice=="2":
                    while True:
                        try:
                            standard = int(input("Enter the standard (1 to 10): "))
                            if 1 <= standard <= 10:
                                print(f"Your standard is: {standard}")
                                break  
                            else:
                                print("Enter a valid standard between 1 and 10.")
                        except ValueError:
                            print("Please enter a valid number.")

                    # print(f"Student in standard {standard} and subject {subject}: ")
                    if standard not in st_name:
                        print(f"No students found for standard {standard}.")
                    else:
                        print(f"Students in standard {standard}:")
                        for student in st_name[standard]:
                            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")
                        
                    student_update=input("Enter the Student roll number of name to Update: ")
                    if student_update.isdigit():
                        student_update = int(student_update)
                    for student in st_name[standard]:
                        if student["roll_number"] == student_update:  
                            new_name = input("\nEnter a new name: ")
                            student["name"] = new_name
                            print(f"Student's name updated to {new_name}.")
                            found=True
                            break
                    if not found:
                        print("Student not found.")
                    else:
                        print(f"\nUpdated list of students in standard {standard}:")
                        for student in st_name[standard]:
                            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")
                                        

                elif choice=="3":
                    while True:
                        try:
                            standard = int(input("Enter the standard (1 to 10): "))
                            if 1 <= standard <= 10:
                                print(f"Your standard is: {standard}")
                                break  
                            else:
                                print("Enter a valid standard between 1 and 10.")
                        except ValueError:
                            print("Please enter a valid number.")
                    
                    if standard not in st_name:
                        print(f"No students found for standard {standard}.")
                    else:
                        print(f"Students in standard {standard}:")
                        for student in st_name[standard]:
                            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")
                        
                    student_delete=input("Enter the Student Roll Number to Delete: ")
                    if student_delete.isdigit():
                        student_delete = int(student_delete)
                    for student in st_name[standard]:
                        if student["roll_number"] == student_delete: 
                            st_name[standard].remove(student)
                            print(f"\nStudent {student_delete} removed from {subject} in Standard {standard}.")
                            found=True
                            break
                    if not found:
                        print("Student not found.")
                    else:
                        print(f"\nUpdated list of students in standard {standard}:")
                        for student in st_name[standard]:
                            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")


                elif choice == "4":
                    while True:
                        try:
                            standard = int(input("Enter the standard (1 to 10): "))
                            if 1 <= standard <= 10:
                                print(f"Your standard is: {standard}")
                                break  
                            else:
                                print("Enter a valid standard between 1 and 10.")
                        except ValueError:
                            print("Please enter a valid number.")

                    print(f"Students in standard {standard}:")
                    if st_name[standard]:
                        for student in st_name[standard]:
                            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")
                    else:
                        print(f"No students found in standard {standard}.")

                elif choice=="5":
                    break
                    
                else:
                    print("Invaild choice")
                

    def student_marks_manage(standard, st_subject, st_name):

        while True:
            print("\n1.Add Marks ")
            print("2.Update Marks ")
            print("3.Delete Marks ")
            print("4.View Marks ")
            print("5.MainMenu ")
            choice = input("Enter your choice for student marks (1 to 5): ")

            if choice == "1":  
                while True:
                    try:
                        standard = int(input("Enter the standard (1 to 10): "))
                        if 1 <= standard <= 10:
                            print(f"Your standard is: {standard}")
                            break
                        else:
                            print("Enter a valid standard between 1 and 10.")
                    except ValueError:
                        print("Invalid input! Please enter a number between 1 and 10.")

                # Display students in the selected standard
                print(f"\nStudents in standard {standard}:")
                if standard in st_name and st_name[standard]:
                    for student in st_name[standard]:
                        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")
                else:
                    print("No students found in this standard.")
                    return  # Exit if no students found

                # Input student roll number
                student_roll_number = input("\nEnter student roll number: ").strip()
                if student_roll_number.isdigit():
                    student_roll_number = int(student_roll_number)

                found = False
                for student in data.st_name[standard]:
                    if student.get("roll_number") == student_roll_number:
                        student.setdefault("marks", {})  # Ensure 'marks' key exists
                        
                        for subject in data.st_subject.get(standard, []):
                            while True:
                                marks = input(f"Enter marks for {subject}: ").strip()
                                if marks.isdigit() and int(marks) >= 0:
                                    student["marks"][subject] = int(marks)
                                    # print(f"Marks add for student {student['name']}")
                                    break
                                else:
                                    print("Invalid input! Please enter a non-negative number.")
                        print(f"Marks add for student {student['name']}")
                        # print("All subject marks added successfully!")
                        found = True
                        break

                if not found:
                    print("Student not found. Please check the roll number.")
                else:
                        print(f"\nUpdated list of students in standard {standard}:")
                        for student in st_name[standard]:
                            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, marks:{student['marks']}")


            elif choice == "2": 
                while True:
                    try:
                        standard = int(input("Enter the standard (1 to 10): "))
                        if 1 <= standard <= 10:
                            print(f"Your standard is: {standard}")
                            break
                        else:
                            print("Enter a valid standard between 1 and 10.")
                    except ValueError:
                        print("Invalid input! Please enter a number between 1 and 10.")

                print("Student names:")
                for student in st_name[standard]:
                    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")

                student_name = input("\nEnter the Student roll number: ").strip()
                if student_name.isdigit():
                        student_name = int(student_name)

                found=False
                for student in st_name[standard]:
                    if student["roll_number"] == student_name:  # Ensure correct student
                        if "marks" not in student:  # Initialize 'marks' key if missing
                            student["marks"] = {}
                        for subj in st_subject[standard]:
                            while True:
                                marks = input(f"Enter marks for {subj}: ").strip()
                                if marks=="":
                                    print(f"Skipping {subj}")
                                    break
                                elif marks.isdigit() and int(marks) >= 0:
                                    student["marks"][subj] = int(marks)
                                    break
                                else:
                                    print("Invalid input! Please enter a non-negative number.")
                        print(f"Marks updated for roll number {student_name}.")
                        found = True
                        break
                if not found:
                    print("Student not found. Please check the roll number.")
                else:
                        print(f"\nUpdated list of students in standard {standard}:")
                        for student in st_name[standard]:
                            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Marks:{student['marks']}")


            elif choice == "3":
                while True:
                    try:
                        standard = int(input("Enter the standard (1 to 10): "))
                        if 1 <= standard <= 10:
                            print(f"Your standard is: {standard}")
                            break
                        else:
                            print("Enter a valid standard between 1 and 10.")
                    except ValueError:
                        print("Invalid input! Please enter a number between 1 and 10.")

                if standard in st_subject:
                    print("Available subjects for your standard:")
                    for index, subject in enumerate(st_subject[standard], start=1):
                        print(f"{index}. {subject}")
                else:
                    print(f"No subjects found for standard {standard}.")
                    return  # Exit if no subjects found

                while True:
                    try:
                        select_subject = int(input("\nEnter your Subject (1 to 5): "))
                        if 1 <= select_subject <= len(st_subject[standard]):
                            new_subject = st_subject[standard][select_subject - 1]
                            print(f"You selected this subject: {new_subject}")
                            break  # Exit loop after successful selection
                        else:
                            print(f"Enter a valid subject number between 1 and {len(st_subject[standard])}.")
                    except ValueError:
                        print("Invalid input! Please enter a number between 1 and 5.")

                print(f"Student name: ")
                for student in st_name[standard]:
                    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")

                student_name = input("\nEnter the Student Name: ")
                if student_name.isdigit():
                        student_name = int(student_name)
                for student in st_name[standard]:
                    if student["roll_number"] == student_name:
                        if "marks" not in student:  # Initialize 'marks' key if missing
                            student["marks"] = {}
                        # if subject in student["marks"]:
                        del student["marks"][subject]
                        print(f"Marks deleted for {student_name}")
                        found=True
                        break
                if not found:
                    print("Student not found. Please check the roll number.")
                else:
                        print(f"\nUpdated list of students in standard {standard}:")
                        for student in st_name[standard]:
                            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Marks:{student['marks']}")


            elif choice == "4":
                while True:
                        try:
                            standard = int(input("Enter the standard (1 to 10): "))
                            if 1 <= standard <= 10:
                                print(f"Your standard is: {standard}")
                                break  
                            else:
                                print("Enter a valid standard between 1 and 10.")
                        except ValueError:
                            print("Please enter a valid number.")

                    
                print("\nMarks:")
                for student in st_name[standard]:
                    print(f"Roll Number: {student['roll_number']}, {student['name']}: {student.get('marks', 'No marks assigned')}")
                    
            elif choice == "5":
                break

            else:
                print("Invalid choice")

    def student_percentage_grade(standard, st_name):

        while True:
            print("1.View Marks ")
            print("2.View Grade ")
            print("3.MainMenu ")
            choice = input("\nEnter your choice for student marks (1 to 3): ")

            if choice == "1":
                while True:
                    try:
                        standard = int(input("Enter the standard (1 to 10): "))
                        if 1 <= standard <= 10:
                            print(f"Your standard is: {standard}")
                            break
                        else:
                            print("Enter a valid standard between 1 and 10.")
                    except ValueError:
                        print("Invalid input! Please enter a number between 1 and 10.")

                for student in st_name[standard]:
                        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")
                student_name = input(f"Enter the roll nmuber of the student to view their details: ")
                student_found = False

                if student_name.isdigit():
                        student_name = int(student_name)
                for student in st_name[standard]:
                    if student["roll_number"] == student_name:
                        student_found = True
                        print(f"Name: {student['name']}")
                        marks = student.get("marks", None)
                        if marks:
                            print(f"Marks: {marks}")
                        else:
                            print("Marks: Not yet assigned.")
                        break
                
                if not student_found:
                    print(f"Student {student_name} not found in standard {standard}.")
            
            elif choice == "2":
                while True:
                    try:
                        standard = int(input("Enter the standard (1 to 10): "))
                        if 1 <= standard <= 10:
                            print(f"Your standard is: {standard}")
                            break
                        else:
                            print("Enter a valid standard between 1 and 10.")
                    except ValueError:
                        print("Invalid input! Please enter a number between 1 and 10.")

                if standard in st_name:
                    print(f"\nStudents in Standard {standard}:")
                    for student in st_name[standard]:
                        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")
                    student_name = input("\nEnter the Student Roll number: ")

                    if student_name.isdigit():
                        student_name = int(student_name)
                    for student in st_name[standard]:
                        if student["roll_number"] == student_name:
                            student_found = True
                            print(f"Name: {student['name']}")
                            marks = student.get("marks", None)
                            if marks:  
                                total_marks = sum(int(mark) for mark in marks.values())
                                num_subjects = len(marks)
                                percentage = (total_marks / (num_subjects * 100)) * 100
                                if percentage <=33:
                                    print(f" F Grade for {percentage} percentage") 
                                elif percentage <=45:
                                    print(f" E Grade for {percentage} percentage")
                                elif percentage <=60:
                                    print(f" D Grade for {percentage} percentage")
                                elif percentage <=75:
                                    print(f" C Grade for {percentage} percentage")
                                elif percentage <=90:
                                    print(f" B Grade for {percentage} percentage")
                                elif percentage <=100:
                                    print(f" A Grade for {percentage} percentage")
                            break
                    else:
                        print(f"No data found for standard {standard}.")
    
            elif choice == "3":
                break

            else:
                print("Invalid choice")

def adminlogin():
    login = admin_module.admin_login()  

    if login:
        # if hasattr(data, "st_name") and data.st_name:  
        #     admin_module.gr_number(data.st_name)  
            
            
            standards = list(data.st_name.keys()) 
            subjects = data.st_subject  

            if all(hasattr(data, attr) for attr in ["st_name", "st_subject"]):
                admin_module.selection(standards, subjects, data.st_name, data.st_subject)
            else:
                print("Error: Data attributes missing or not initialized.")
            # else:
            #     print("Error: No student data available.")

if __name__ == "":
    adminlogin()
