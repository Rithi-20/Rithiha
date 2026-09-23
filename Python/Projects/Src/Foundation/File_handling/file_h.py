# ct=3
# while ct>=0:
#     std=input("Enter you name: ")
#     ct-=1

# r "" used because without it it takes as unicode r says it is a string
file=open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt","r")
print(file.read())
#open --> should be closed using file.close()

# to work with the file that is already opened . When the file does not exist it shows an error . Pointer starts at beginning
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt","r") as file:
    content=file.read()  # --> read - read entire content. It takes \n automatically 
    print(content)

# with open ----> it will open the file and close it automatically 

# how many characters to read
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt", "r") as file:
    content = file.read(7)
    print(content)


#  Append the content to the existing file
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt","a") as file:
    content="Keerthana"
    file.write(content)  # --> write - write a string to a file . It does not automatically add new line
    print("Done")


#write - if the file does not exist it creates new one and write or completely replace with the new content if exists
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt","w") as file:
    file.write("Nishanth")


# r+ =executes both read and write . unlike write it does not replace complete file . it just replaces based on word length
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt","r+") as file:
    file.write("Keerthana")
    content=file.read()
    print(content)

# w+ - it uses both read and write. It clears existing file first and then replace with new data . if the file does not exist it creates new one 
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt", "w+") as file:
    file.write("Keerthana")
    file.seek(0)   # it moves the pointer to 1
    print(file.read())


# it performs both append and read 
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt", "a+") as file:
    file.write("\nVasundraa")
    file.seek(0)
    print(file.read())

# readlines()- read all lines and return the list of strings . it keeps the new line character in the result
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt", "r") as file:
    content = file.readlines()  # it will show the result as list 
    print(content)


# it allows multiple datas to be written in the file . It does not add \n auto,atically
students = ["Rithiha\n", "Mithra\n", "Vasu\n"]
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt", "w") as file:
    file.writelines(students)

# it reads only one line at a time 
with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\std_details.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.tell()) # --> It shows the current pointer
