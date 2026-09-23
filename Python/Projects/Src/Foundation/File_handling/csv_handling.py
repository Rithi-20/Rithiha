import csv

with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\data.csv","r") as file:
    reader=csv.reader(file)  # here reader acts as a cursor
    for line in file:    # To iterate through data and to print it and it will print exactly how it is present in the csv file 
        print(line)
    # print(reader)  # It prints address


    reader=csv.DictReader(file)   # dict reader will help to treat as dictionary and to display the data
    for i in reader:
        print(i["Name"],i["Dept"]) # or print(i["Dept"])


with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\data.csv","w") as file:
    # To write an content in csv file
    writer=csv.writer(file)
    writer.writerow(["Nishanth","Automobile"])


with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\data.csv","a",newline="") as file:
    # To add an content in csv file
    writer=csv.writer(file)
    writer.writerow(["Nishanth","Automobile"])


# to write multiple rows
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\data.csv","a",newline="") as file:
    writer=csv.writer(file)
    writer.writerows([["Nishanth","Automobile"],["Sri","IT"]])

# dictwriter using write row
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\data.csv","w",newline="") as file:
    fieldname=["Name","Dept"]
    writer=csv.DictWriter(file,fieldnames=fieldname)
    writer.writeheader()
    writer.writerow({"Name":"a","Dept":"Cse"})


# dictwriter using write rows
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\data.csv","w",newline="") as file:
    fieldname=["Name","Dept"]
    writer=csv.DictWriter(file,fieldnames=fieldname)
    writer.writeheader()  # header - is used to set header and is used in DictWriter
    writer.writerows([
        {"Name": "Nishanth", "Dept": "Automobile"},
        {"Name": "Sri", "Dept": "IT"},
        {"Name": "Ravi", "Dept": "CSE"},
        {"Name": "Priya", "Dept": "ECE"}
    ])

# or

students = [
    {"Name": "Nishanth", "Dept": "Automobile"},
    {"Name": "Sri", "Dept": "IT"},
    {"Name": "Ravi", "Dept": "CSE"},
    {"Name": "Priya", "Dept": "ECE"}
]
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\data.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Name", "Dept"]
    )
    writer.writeheader() # it is present only with dictwriter
    for student in students:
        writer.writerow(student)





