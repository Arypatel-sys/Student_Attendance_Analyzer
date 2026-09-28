from student import students

def calculateattendance():
    print("\n===attendance calculation===")
    if len(students)== "0":
        print("no student added yet")
    else:
         for student in students:
             totalclasses=(student[3])
             attendedclasses=(student[4])
             if totalclasses==0:
                 print("\nstudent name:",student[0])
                 print("attendasnce cannot caltulate")
             else:

                 attendance=(attendedclasses/totalclasses)*100
                 print("\nstudent name:",student[0])
                 print("roll number:",student[1])
                 print("attendance:",round(attendance , 4), "%")