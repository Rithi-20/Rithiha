import json

# | Function  | Input           | Output          |
# | --------- | --------------- | --------------- |
# | `dump()`  | Python object   | JSON **file**   |
# | `dumps()` | Python object   | JSON **string** |
# | `load()`  | JSON **file**   | Python object   |
# | `loads()` | JSON **string** | Python object   |

# to load and display data
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_data.json","r") as j_file:
    student=json.load(j_file)
    print(student["marks"]["Python"])


# to add data use dump  - it appends as seperate dict
data={"Present":"Yes"}
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_data.json","a") as j_file:
    student=json.dump(data,j_file,indent=2)
    print(student)


# to add data use dump  - it appends to the existing dictionary
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_data.json", "r") as j_file:
    student = json.load(j_file)

student["Present"] = "Yes"

with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_data.json", "w") as j_file:
    json.dump(student, j_file, indent=2)


# dumps - dumps will stire as string
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_data.json", "r") as j_file:
    l=json.load(j_file)
result = json.dumps(l)
print(result)


# json.loads() --> json string to python object
data = '{"name": "Arun", "marks": 90}'
student = json.loads(data)
print(student)
print(type(student))






   
