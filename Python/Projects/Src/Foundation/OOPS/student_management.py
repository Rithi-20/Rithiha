# class Student:
#     university="Nova University"
#     def __init__(self,name,id,dept,marks,att):
#         self.name=name
#         self.id=id
#         self.dept=dept
#         self.marks=marks
#         # protect
#         self._att=att #encapsulation -> attendance is protected and will not show because it hides so to see use getter and setter
#         if 0 <= att <= 100:
#             self._att=att
#         else:
#             raise ValueError("Please enter valid number") # Inside init return or print will not be allowed 
                        

#     def display(self):
#         return f"Name:{self.name} \nID:{self.id} \nDepartment:{self.dept} \nMarks:{self.marks} \nAttendance:{self._att} "


#     def average(self):
#         return f"Average:{sum(self.marks)//len(self.marks)}"

#     #getter - this will display the attendance when it is given
#     def get_attendance(self):
#         return self._att

#     #setter - this will set the condition for attendance
#     def set_attendance(self,value):
#         if 0 <= value <= 100:
#             return value
#         else:
#             # raise ValueError("Please enter valid number")
#             return "Please enter valid number"


# std1=Student("Arun","CS101","CSE",[89,90,89],90)
# std2=Student("Varun","IT101","IT",[90,99,89],90)
# print(std1.display())



#------------------------------------------------------------------------------------------------------------------------------------------
# Do not display the marks and calcuate the cgpa 
#---------------------------------------------------------------------------------------------------------------------------------------------------

class Student:
    university="Nova University"
    def __init__(self,name,id,dept,marks,att):
        self.name=name
        self.id=id
        self.dept=dept
        
        self._marks=marks
        self.set_marks()
         
        # protect
        self._att=att #encapsulation -> attendance is protected and will not show because it hides so to see use getter and setter
        if 0 <= att <= 100:
            self._att=att
        else:
            raise ValueError("Please enter valid number") # Inside init return or print will not be allowed 

            

    def display(self):
        return f"Name:{self.name} \nID:{self.id} \nDepartment:{self.dept} \nAttendance:{self._att} \nCGPA:{self.CGPA()}"
   

    def average(self):
        return f"Average:{sum(self._marks)//len(self._marks)}"

    #getter - this will display the attendance when it is given
    def get_attendance(self):
        return self._att

    #setter - this will set the condition for attendance
    def set_attendance(self,value):
        if 0 <= value <= 100:
            return value
        else:
            # raise ValueError("Please enter valid number")
            return "Please enter valid number"

    def CGPA(self):
        avg=sum(self._marks)//len(self._marks)
        self.cgpa=round((avg/10),2)
        return self.cgpa

    def set_marks(self):
        for i in self._marks:
            if not 0<=i<=100:
                raise ValueError("Enter the marks between 0 to 100")



std1=Student("Arun","CS101","CSE",[89,90,100],90)
std2=Student("Varun","IT101","IT",[90,99,89],90)

print(std1.display())



#---------------------------------------------------------------------------------------------------------------------------------------------
#To display all the values stored
#------------------------------------------------------------------------------------------------------------------------------------------------------
# class Student:
#     university="Nova University"
#     def __init__(self,name,id,dept,marks,att):
#         self.name=name
#         self.id=id
#         self.dept=dept
#         self._marks=marks
#         # protect
#         self._att=att #encapsulation -> attendance is protected and will not show because it hides so to see use getter and setter
#         if 0 <= att <= 100:
#             self._att=att
#         else:
#             raise ValueError("Please enter valid number") # Inside init return or print will not be allowed 

            

#     def display(self):
#         return f"Name:{self.name} \nID:{self.id} \nDepartment:{self.dept} \nAttendance:{self._att} \nMarks:{self._marks} \nCGPA:{self.CGPA()}"
        

#     def average(self):
#         return f"Average:{sum(self._marks)//len(self._marks)}"

#     #getter - this will display the attendance when it is given
#     def get_attendance(self):
#         return self._att

#     #setter - this will set the condition for attendance
#     def set_attendance(self,value):
#         if 0 <= value <= 100:
#             return value
#         else:
#             # raise ValueError("Please enter valid number")
#             return "Please enter valid number"

#     def CGPA(self):
#         avg=sum(self._marks)//len(self._marks)
#         self.cgpa=round((avg/10),2)
#         return f"CGPA:{self.cgpa}"

#     def set_marks(self):
#         for i in self._marks:
#             if 0<=self._marks[i]<=100:
#                 self._marks=self._marks
#             else:
#                 return "Enter the marks between 0 to 100"


# #  To iterate and display all the details
# stds=[]
# num=0
# m=[]
# while len(stds)<2:
#     n=input("Enter your name: ")
#     id=input("Enter your ID: ")
#     dept=input("Enter your Department: ")
#     for i in range(3):
#         ma=int(input(f"Enter your marks for sub{i+1}: "))
#         m.append(ma)
#     att=int(input("Enter your attendance: "))
#     std=Student(n,id,dept,m,att)
#     stds.append(std)

# for i in range(len(stds)):
#     print(stds[i].display())


        
