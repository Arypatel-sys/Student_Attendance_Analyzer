
from student import students
def attendancereport():
    print("\n===attendance report")
    if len(students)== 0 :

     print("no student added yet")
        
    else:
        for student in students:
            totalclasses=student[3]
            attendedclasses=student[4]

            if totalclasses == 0:
               print("\nstudent name:",student[0])
               print("attendance cannot calculate")

            else:
               attendance=(attendedclasses/totalclasses)*100

               print("\nstudent name:",student[0])
               print("rollnumber:",student[1])
               print("regitrationnumber:",student[2])
               print("attendance:",round(attendance,4) , "%")

               if attendance >=75:
                  print("status: eligeble")
               else:
                  print("status:not eligeble")

