#value error

# i/p = 20 , o/p= 20
# i/p=Twenty, o/p= Value error
try:
    age=int(input("Enter age: "))
    print(age)

except ValueError:
    print("Please enter a age in numbers")



# file not found
try:
    with open(r"student.txt","r") as file:
        file.read()

except FileNotFoundError:
    print("File does not exist please create file ")



# #permission error  -  icacls "D:\Rithiha\Python\Projects\Src\Foundation\File_handling\data.csv" /deny "$env:USERNAME`:R" - ony read permission is given to this file path
try:
    with open(r"D:\Rithiha\Python\Projects\Src\Foundation\File_handling\data.csv", "r") as file:
        data = file.read()
        # file.write()   
        # # or
        print(data)

except PermissionError:
    print("You can only read this file and it cannot be written")


# File error:
# File not found
# Permission error
# FileExists error - when file is already exist and you try to create new file it shows this error
# IsADirectory error - tried to open directory as a file

# When we dont know what is the error so we can use just except
try:
    age=int(input("Enter age: "))
    print(age)

except:
    print("Please enter a age in numbers")


# else - when the try is success the else block will be executed or else. When the try is failed then else bock will not be executed
try:
    age=int(input("Enter age: "))

except ValueError:
    print("Please enter a age in numbers")

else:
    print("Please enter a valid number")



# finally- It executes always
try:
    age=int(input("Enter age: "))
    print(age)

except:
    print("Please enter a age in numbers")

finally:
    print("Success")


# except - used when python detectes error
# raise - used when application needs to detect the error(simply can create custom errors). 


# when the attendance is valid stop it or else continue the program
while True:
    try:
        att=float(input("Enter attendance: "))
        if not 0<=att<=100:
            raise ValueError("Enter attendance between 0 to 100")
        else:
            print("Attendance",att)
        break

    except ValueError:
        print("Invalid attendance")

