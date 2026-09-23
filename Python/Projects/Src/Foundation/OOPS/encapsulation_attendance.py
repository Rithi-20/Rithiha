class Student:
    university="Nova University"
    def __init__(self,name,id,dept,marks,att):
        self.name=name
        self.id=id
        self.dept=dept
        self.marks=marks
        # protect
        self._att=att #encapsulation -> attendance is protected and will not show because it hides so to see use getter and setter
        if 0 <= att <= 100:
            self._att=att
        else:
            raise ValueError("Please enter valid number") # Inside init return or print will not be allowed 
                        

    def display(self):
        return f"Name:{self.name} \nID:{self.id} \nDepartment:{self.dept} \nMarks:{self.marks} \nAttendance:{self._att} "


    def average(self):
        return f"Average:{sum(self.marks)//len(self.marks)}"

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


std1=Student("Arun","CS101","CSE",[89,90,89],90)
std2=Student("Varun","IT101","IT",[90,99,89],90)
print(std1.display())