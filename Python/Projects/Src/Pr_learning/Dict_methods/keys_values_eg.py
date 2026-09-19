# Keys example 
#string
student = {
    "Name": "Rithiha",
    "Age": 21
}

print(student["Name"])

#int
student = {
    101: "Arun",
    102: "Priya",
    103: "Rahul"
}

print(student[101])


#Float as a key
data = {
    1.5: "Value A",
    2.5: "Value B"
}

print(data[1.5])

# Tuple as a key
locations = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}

print(locations[(10, 20)])

#=====================================================================================================================

#values
#String
student = {
    "name": "Rithiha",
    "course": "AI"
}


#Int
student = {
    "age": 21,
    "roll_no": 27
}


#Float
student = {
    "credits": 8.32,
    "percentage": 85.5
}


#Bolean
student = {
    "is_completed": True,
    "is_placed": False
}


#list
student = {
    "subjects": ["Python", "AI", "Maths"]
}


#Tuple
student = {
    "coordinates": (10, 20)
}

#Set
student = {
    "skills": {"Python", "Java", "SQL"}
}


#Nested dict
student = {
    "personal_details": {
        "name": "Rithiha",
        "age": 21
    }
}