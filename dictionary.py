"""
students = {}
marks = list()
temp = {}
n = int(input("entre the no of students"))
for i in range(1, n+1):
    marks.clear()
    temp["name"] = input("enter a name")
    temp["rollno"] = input("enter roll no")
    sum = 0
    for m in range(1, 3):
        ma = int(input("enter marks"))
        marks.append(ma)
        sum = sum+ma
        temp["total"] = sum
    print(marks)
    temp["marks"] = marks
    students[i] = temp
    print(students)


for key in students.keys():
    print(key, students[key])
"""

students = {}
marks = []
n = int(input("Enter no of students"))
for i in range(1, n+1):
    name = input("enter a name")
    rollno = int(input("enter roll no"))
    sum = 0
    marks.clear()
    for m in range(1, 3):
        ma = int(input("enter marks"))
        marks.append(ma)
        sum = sum+ma
        students.update({
            name: {
                "rollno": rollno,
                "marks": marks,
                "total": sum,
                "average": sum/3
            }

        })
for key in students:
    print(key, students[key])

"""
------------------------------------------------------

students = {}
marks = list()
temp = {}
n = int(input("entre the no of students"))
for i in range(1, n+1):
    marks.clear()
    temp["name"] = input("enter a name")
    temp["rollno"] = input("enter roll no")
    temp["marks"] = marks
    for m in range(0, 3):
        ma = int(input("enter marks"))
        marks.append(ma)

    temp["total"] = marks[0]+marks[1]+marks[2]
    students[i] = temp
    print(students)


for key in students.keys():
    print(key, students[key])
"""
