from student import students


def calculateattendance():

    print("===attendance calculation===")

    if len(students) == 0:

        print("no student added yet")

    else:

        for student in students:

            totalclasses = student[3]
            attendedclasses = student[4]

            if totalclasses == 0:

                print("student name:", student[0])
                print("attendance cannot calculate")

            else:

                attendance = (attendedclasses / totalclasses) * 100

                print("student name:", student[0])
                print("roll number:", student[1])
                print("attendance:", round(attendance, 2), "%")