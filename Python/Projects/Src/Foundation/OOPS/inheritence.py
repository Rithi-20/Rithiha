class Person:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    #polymorphism- same method used in different methods
    def display_role(self):
        return "University Person"

class Student(Person): # inherited from above class 
    def __init__(self,name,email,dept):
        super().__init__(name,email) # To inherit from a parentor super class  we use super and will use the init from Person class. The name,email can be reused
        self.dept=dept

    #polymorphism
    def display_role(self):
        return "Student"


class Teacher(Student):
    def __init__(self,name,email,dept,sub_handled): 
        super().__init__(name,email,dept) # inherited from student init . The name,email , dept can be reused
        self.sub_handled=sub_handled

    #polymorphism
    def display_role(self):
        return "Teacher"

st1=Student("rithi","rithi@gmail.com","cse")
print(st1.display_role()) 

people=[
    Student("rithi","rithi@gmail.com","cse"),
    Teacher("vasu","vasu@gmail.com","cse",["ai","cse"])
]
for person in people:
    print(person.display_role())


