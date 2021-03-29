d = dict()
while True:
    ch = int(input(
        "\n 1 to add student \n 2 - print all student details \n 3 - find an student by name \n 0-exit \n"))
    if ch == 1:
        name = input("enter student name\n")
        address = input("enter address\n")
        semester = input("enter semester\n")
        marks = []
        total = 0
        for m in range(0, 5):
            ma = int(input("enter marks"))
            marks.append(ma)
            total = total+ma
        percent = (total/250)*100
        if percent > 80:
            grade = "A"
        elif percent > 60 and percent < 80:
            grade = "B"
        else:
            grade = "C"
        d.update({name: {
            "name": name,
            "address": address,
            "semester": semester,
            "marks": marks,
            "total": total,
            "percent": percent
        }})
    elif ch == 2:
        for key in d:
            print(key, d[key])
    elif ch == 3:
        name = input("enter the name of the employee to be searched")
        for key in d:
            if key == name:
                print("employee found")
                for i in d[key]:
                    print(i, d[key][i])
                    flag = 1
        if flag == 0:
            print("no record found")
    elif ch == 0:
        break
        print("thank you for using student result mangement system")
