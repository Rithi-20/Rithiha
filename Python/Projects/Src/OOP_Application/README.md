# Nova University – Student Management Module

## 1. Project Overview

The **Nova University Student Management Module** is a Python console application that maintains student and faculty information and supports basic academic checks. It uses Object-Oriented Programming (OOP) to organize student and faculty details and their related behaviours.

## 2. Business Problem

Nova University needs a simple application to manage student and faculty records, review student academic information, calculate academic results, and check examination eligibility based on attendance.

This application provides a menu-driven way to add and view student and faculty details, check attendance eligibility, and display a student's academic result.

## 3. Features

- Add and view multiple student records.
- Store student ID, name, email, phone, department, attendance, and Python, SQL, and Excel marks.
- Check examination eligibility using attendance.
- Calculate total marks and average marks.
- Determine pass/fail status and assign a grade.
- Add and view faculty records, including faculty ID, contact details, department, designation, subject, and experience.
- Handle invalid menu choices and invalid numeric input.
- Validate attendance and marks within the range of 0 to 100.

## 4. Business Rules

- **Attendance range:** 0–100.
- **Examination eligibility:** Attendance of 75% or above means the student is eligible.
- **Pass rule:** An average mark of 50 or above is considered a pass.
- **Total marks:** Sum of Python, SQL, and Excel marks.
- **Average marks:** Total marks divided by 3.
- **Grade scale:**

| Average Marks | Grade |
|---|---|
| 90 and above | A |
| 80–89.99 | B |
| 70–79.99 | C |
| 60–69.99 | D |
| 50–59.99 | E |
| Below 50 | F |

## 5. Design Approach and OOP Concepts

The application uses two classes:

- **`Student`** – Stores student details and subject marks. It includes methods to calculate total and average marks, determine pass/fail status and grade, validate marks and attendance, check examination eligibility, and display student information.
- **`Teacher`** – Stores and displays faculty information, including ID, name, email, phone, department, designation, subject, and experience.

The application stores student objects in a `students` list and faculty objects in a `teachers` list. A loop displays the menu repeatedly, and a `match` statement handles the selected operation.

### OOP concepts used

- **Classes and objects:** `Student` and `Teacher` define the structure of records; objects represent individual students and faculty members.
- **Encapsulation:** Related attributes and behaviours are grouped within their respective classes.
- **Methods:** Class methods perform display, validation, academic calculations, and eligibility checks.
- **Reusable logic:** Academic calculations and validation are defined as methods rather than repeated throughout the menu.

The current implementation does not use inheritance or polymorphism.

## 6. How the Application Works

When the program starts, it displays a menu:

1. Add Student
2. View Students
3. Check Attendance Eligibility
4. View Academic Result
5. Add Faculty
6. View Faculty
7. Exit

The user selects an option and enters the requested details. Student and faculty objects are stored in their respective lists for the current session. Student records can then be viewed, searched by ID for eligibility or result checks, and evaluated using the academic rules. The application continues displaying the menu until the user selects Exit.

**Note:** Records are stored in memory and are not saved permanently after the program closes.

## 7. Project Structure

```text
OOP_Application/
├── OOP.py
├── README.md
└── Output/
    ├── Academic result
    ├── Add faculty
    ├── Add Student
    ├── Check eligibility
    ├── View Faculty
    └── View student
```

The screenshot names above are shown as they appear in the `Output` folder. If your screenshot files have extensions such as `.png` or `.jpg`, keep those extensions in the actual filenames.

## 8. Application Screenshots

The screenshots below use relative paths from the repository root. These links assume the image files are PNGs. If your files have a different extension, change the extension in each path to match the actual file.

### Academic Result
![Academic Result](Output/Academic%20result.png)

### Add Faculty
![Add Faculty](Output/Add%20faculty.png)

### Add Student
![Add Student](Output/Add%20Student.png)

### Check Eligibility
![Check Eligibility](Output/Check%20eligibility.png)

### View Faculty
![View Faculty](Output/View%20Faculty.png)

### View Student
![View Student](Output/View%20student.png)

## 9. How to Run

### Prerequisites

Install Python 3.

Check that Python is installed:

```bash
python --version
```

### Run the application

1. Open a terminal in the project folder.
2. Run:

```bash
python OOP.py
```

3. Follow the menu instructions.

If your Python file has a different name, replace `OOP.py` with that filename.

## 10. Conclusion

The Nova University Student Management Module demonstrates how Python classes and objects can be used to organize student and faculty records, validate attendance and marks, calculate academic performance, and check examination eligibility in a simple console application.
