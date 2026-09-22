from abc import ABC,abstractmethod
class Person:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    # abstract method is used to hide the internal operations and also must operations can be done. 
    # here abstract method is given when this class is inherited somewhere this method must there or else it will show an error 
    @abstractmethod
    def display_role(self):
        return "University Person"

    @abstractmethod
    def display_dashboard(self):
        pass

class Student(Person): # inherited from above class 
    def __init__(self,name,email,dept):
        super().__init__(name,email) # To inherit from a parentor super class  we use super and will use the init from Person class. The name,email can be reused
        self.dept=dept

    #polymorphism
    def display_role(self):
        return "Student"

    def display_dashboard(self):
        return "Student Dashboard"


class Teacher(Student):
    def __init__(self,name,email,dept,sub_handled): 
        super().__init__(name,email,dept) # inherited from student init . The name,email , dept can be reused
        self.sub_handled=sub_handled

    #polymorphism
    def display_role(self):
        return "Teacher"

    def display_dashboard(self):
        return "Teacher Dashboard"

class hod(Person):
    def __init__(self,name,email):
        super().__init__(name,email)

    def display_role(self):
        return "Hod"
    
    def display_dashboard(self):
        return "Teacher Dashboard"

# st1=Student("rithi","rithi@gmail.com","cse")
# print(st1.display_role()) 

hod1=hod("rithi","rithi@gmail.com")
print(hod1.display_dashboard())