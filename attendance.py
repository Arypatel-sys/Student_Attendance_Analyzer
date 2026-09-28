from validation import valid_classes

students = []


def add_student():

    studentname = input("enter the student name:")
    rollnumber = input("enter the roll number:")
    registrationnumber = input("enter the registration number:")
    totalclasses = int(input("enter the total classes:"))
    attendedclasses = int(input("enter the attended classes:"))

    if valid_classes(totalclasses, attendedclasses):

        student = [studentname, rollnumber, registrationnumber, totalclasses, attendedclasses]

        students.append(student)

        print("student added successfully")

    else:

        print("invalid classes details")


def viewstudents():

    if len(students) == 0:

        print("no student added yet")

    else:

        for student in students:

            print("studentname:", student[0])
            print("rollnumber:", student[1])
            print("registrationnumber:", student[2])
            print("totalclasses:", student[3])
            print("attendedclasses:", student[4])