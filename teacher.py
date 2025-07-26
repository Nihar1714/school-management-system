from admin import admin_module
from data_module import data

def teacher():
    def teacher_login():
        user_name = "teacher"
        user_password = "teacher123"

        user = input("Enter Your TeacherName: ")
        password = input("Enter Your Password: ")

        if user == user_name and password == user_password:
            print("Welcome")
            return True 
        else:
            print("Your data is wrong")
            return False 

    if teacher_login():
        if hasattr(data, "st_subject") and hasattr(data, "st_name"):
            standard = None
            admin_module.student_marks_manage(standard,data.st_subject, data.st_name)
        else:
            print("Error: Student data not found. Please check `data.st_subject` and `data.st_name`.")
    else:
        print("Login failed. Exiting program.")