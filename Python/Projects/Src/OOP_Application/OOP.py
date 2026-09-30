class Teacher:
    def __init__(self,Id,Name,Email,Phone,Department,Designation,Subject,Experience):
        self.Id=Id
        self.Name=Name
        self.Email=Email
        self.Phone=Phone
        self.Department=Department
        self.Designation=Designation
        self.Subject=Subject
        self.Experience=Experience

    def display(self):
        return f"Teacher Id: {self.Id} \nName: {self.Name} \nEmail: {self.Email} \nPhone: {self.Phone} \nDepartment: {self.Department} \nDesignation: {self.Designation} \nSubject: {self.Subject} \nExperience: {self.Experience}"


class Student:
    def __init__(self,Id,Name,Email,Phone,Department,Attendance,Python_marks,SQL_marks,Excel_marks):
        self.Id=Id
        self.Name=Name
        self.Email=Email
        self.Phone=Phone
        self.Department=Department
        self.Attendance=self.att(Attendance)  
        self.Python_marks=self.marks(Python_marks)
        self.SQL_marks=self.marks(SQL_marks)
        self.Excel_marks=self.marks(Excel_marks)
        



    def total_marks(self):
        return sum([self.Python_marks,self.SQL_marks,self.Excel_marks])
        # or
        # return self.Python_marks+self.SQL_marks+self.Excel_marks

    def avg_marks(self):
        return self.total_marks()/3

    def status(self):
        if self.avg_marks()>=50:
            return "Pass"
        else:
            return "Fail"

    def grade(self):
        if self.avg_marks()>=90:
            return "Grade: A"
        elif self.avg_marks()>=80:
            return "Grade: B"
        elif self.avg_marks()>=70:
            return "Grade: C"
        elif self.avg_marks()>=60:
            return "Grade: D"
        elif self.avg_marks()>=50:
            return "Grade: E"
        else:
            return "Grade F"

    def att(self,value):
        if 0<=value<=100:
            return value
        else:
            raise ValueError("Please enter a valid attendance between 0 to 100")

    def att_eligibility(self):
        if self.Attendance>=75:
            return "Eligible for exam"
        else:
            return "Not Eligible for exam"

    def marks(self,value):
        if 0<=value<=100:
            return value
        else:
            raise ValueError("Please enter a valid marks between 0 to 100")

    def display(self):
        return f"Student Id: {self.Id} \nName: {self.Name} \nEmail: {self.Email} \nPhone: {self.Phone} \nDepartment: {self.Department} \nAttendance: {self.Attendance} \nPython_marks: {self.Python_marks} \nSQL_marks: {self.SQL_marks} \nExcel_marks: {self.Excel_marks}"
    

students=[]
teachers=[]
while True:
    print("--Welcome--")
    print("Choose the operation that needs to be performed")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Attendance Eligibility")
    print("4. View Academic Result")
    print("5. Add Faculty")
    print("6. View Faculty")
    print("7. Exit")

    try:
        n=int(input("Enter your choice: "))
    except ValueError:
        print("Please enter valid menu number")
        continue


    match n:
        case 1:
            try:  
                Id = input("Enter Student ID: ")
                Name = input("Enter Name: ")
                Email = input("Enter Email: ")
                Phone = input("Enter Phone: ")
                Department = input("Enter Department: ")
                Attendance = float(input("Enter Attendance: "))
                Python_marks = float(input("Enter Python marks: "))
                SQL_marks = float(input("Enter SQL marks: "))
                Excel_marks = float(input("Enter Excel marks: "))
                student = Student(Id, Name, Email, Phone, Department,Attendance, Python_marks, SQL_marks, Excel_marks)
                students.append(student)

                print("Student added successfully")

            except ValueError as e:
                print("Error: ",e)

        case 2:
            if len(students)==0:
                print("No students available")
            else:
                print("\n--------- Students ----------")

                for i in students:
                    print(i.display())


        case 3:
            if len(students)==0:
                print("No students available")

            else:
                Id=input("Enter you Id: ")
                f=False
                for i in students:
                    if i.Id==Id:
                        print(i.att_eligibility())
                        f=True
                        break
                if not f:
                    print("Student not found")

        case 4:
            if len(students)==0:
                print("No students available")
            else:
                Id=input("Enter student Id: ")
                f=False

                for i in students:
                    if i.Id==Id:
                        print("\n---------Academic Results-----------")
                        print("Student ID:", i.Id)
                        print("Name:", i.Name)
                        print("Total Marks:", i.total_marks())
                        print("Average Marks:", i.avg_marks())
                        print("Result:", i.status())
                        print("Grade:", i.grade())

                        f=True
                        break
                if not f:
                    print("Student not found")



        case 5:
            Id = input("Enter Faculty ID: ")
            Name = input("Enter Name: ")
            Email = input("Enter Email: ")
            Phone = input("Enter Phone: ")
            Department = input("Enter Department: ")
            Designation = input("Enter Designation: ")
            Subject = input("Enter Subject: ")
            Experience = input("Enter Experience: ")
            teacher=Teacher(Id, Name, Email, Phone, Department,Designation, Subject, Experience)
            teachers.append(teacher)
            print("Faculty added successfully.")

        case 6:
            if len(teachers) == 0:
                print("No faculty members available.")

            else:
                print("\n-----------Faculty--------------")
                for i in teachers:
                    print(i.display())

        case 7:
            print("Thank you for visiting")
            break
        case _:
            print("Invalid Choice")


