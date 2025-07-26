# Student Management System

A comprehensive, command-line-based Student Management System built with Python. This application allows for the management of student data, including their academic records, marks, and grades, through a role-based access system for Admins, Teachers, and Students. All data is managed locally through Python data structures.

## Key Features

### Admin Role
- **Full Student Management**: Add, update, delete, and view student records in any standard.
- **Marks Management**: Add, update, delete, and view marks for any student in any subject.
- **Performance Overview**: View the percentage and grade for any student to monitor academic performance.
- **Secure Login**: Protected with a unique username and password.

### Teacher Role
- **View Student Data**: Teachers can log in to view and manage marks for students.
- **Simplified Access**: A dedicated login for teachers to access student mark-related functionalities.

### Student Role
- **Personal Data Access**: Students can log in using their unique GR Number and password.
- **View Academic Records**: Check their own marks for all subjects.
- **Track Performance**: View their calculated percentage and overall grade.

## How to Run the Application

1.  **Prerequisites**: Make sure you have Python installed on your system.
2.  **Download Files**: Place all the project files (`login.py`, `admin.py`, `teacher.py`, `student.py`, `data_module.py`) in the same directory.
3.  **Run the Program**: Open a terminal or command prompt, navigate to the directory where you saved the files, and run the main login script:
    ```bash
    python login.py
    ```
4.  **Follow the Prompts**: The application will start and prompt you to select a role to log in.

## Default Login Credentials

Use the following credentials to access the different roles:

-   **Admin**:
    -   Username: `admin`
    -   Password: `admin123`
-   **Teacher**:
    -   Username: `teacher`
    -   Password: `teacher123`
-   **Student**:
    -   **GR Number**: Use any `gr_number` from the `data_module.py` file (e.g., `1001`).
    -   **Password**: The password is `${gr_number}@${FirstName}` (e.g., `1001@Akhankhya`).

## Project Structure

-   `login.py`: The main entry point of the application that handles the role selection and login process.
-   `admin.py`: Contains all the functionalities for the Admin user, including student and marks management.
-   `teacher.py`: Contains the login and functionalities for the Teacher user.
-   `student.py`: Implements the student login, mark viewing, and grade calculation features.
-   `data_module.py`: Acts as a local database, storing all student names, subjects, marks, and credentials in Python dictionaries.
