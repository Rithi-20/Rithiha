# Nova University – Student Management Module

## Project Overview

The Student Management Module is a Python-based console application developed for Nova University. It manages student and faculty information and performs basic academic evaluations using Object-Oriented Programming (OOP) principles.

## Features

- Add and view multiple student records.
- Add and view faculty information.
- Display student academic details.
- Calculate total marks and average marks.
- Determine pass/fail status and grade.
- Check examination eligibility based on attendance.
- Validate attendance values between 0 and 100.
- Handle invalid inputs gracefully.
- Provide a simple menu-driven console interface.

## Business Rules

- **Attendance Validation:** Attendance must be between 0% and 100%.
- **Examination Eligibility:** Students with attendance of 75% or above are eligible for the examination.
- **Pass Criteria:** Students with an average mark of 50 or above are considered passed.
- **Academic Calculation:** Total marks and average marks are calculated using Python, SQL, and Excel marks.
- **Grade Calculation:** Grades are assigned based on the grading rules implemented in the application.

## OOP Concepts

The application uses appropriate OOP concepts based on its implementation, such as:

- **Encapsulation:** Organizes related data and methods within classes.
- **Inheritance:** Can reuse common person information for student and faculty entities.
- **Polymorphism:** Can support role-specific behaviour through shared methods.
- **Abstraction:** Separates essential operations from implementation details.
- **Code Reusability:** Avoids unnecessary duplication of academic calculations and business rules.

Only include the concepts above that are actually implemented in `main.py`.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Command-Line Interface (CLI)
- Git and GitHub

## Project Structure

```text
nova-university-oop/
├── main.py
└── README.md
```

- `main.py` – Contains the application source code and menu-driven functionality.
- `README.md` – Provides project documentation and execution instructions.

## How to Run

### Prerequisites

Install Python 3 on your system.

Check the installation:

```bash
python --version
```

### Execution Steps

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/nova-university-oop.git
```

2. Navigate to the project directory:

```bash
cd nova-university-oop
```

3. Run the application:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

4. Follow the console menu to manage student and faculty information.

Replace `YOUR_USERNAME` with your GitHub username.

## Application Menu

The application is designed to provide options for:

1. Add Student
2. View Students
3. Check Attendance Eligibility
4. View Academic Result
5. Add Faculty
6. View Faculty
7. Exit

The available options should match the menu implemented in `main.py`.

## Conclusion

The Nova University Student Management Module demonstrates the practical application of Python OOP concepts to manage academic information, validate inputs, calculate student results, and determine examination eligibility through a simple console application.

**Project:** Nova University OOP Application Activity  
**Language:** Python
