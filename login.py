from admin import adminlogin 
from teacher import teacher
from student import student_login

def main():
    while True:
        print("\nSelect your role:")
        print("1. Admin Login")
        print("2. Teacher Login")
        print("3. Student Login")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1": 
            if adminlogin():
                print("Admin logged in successfully.")
            else:
                print("Admin login failed. Please try again.")
        elif choice == "2":
            if teacher():
                print("Teacher logged in successfully.")
            else:
                print("Teacher login failed. Please try again.")
        elif choice == "3":
            if student_login():
                print("Student logged in successfully.")
            else:
                pass
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
