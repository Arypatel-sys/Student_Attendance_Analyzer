
from student import add_student,viewstudents
from attendance import calculateattendance
from report import attendancereport

while True:

    print("===student attendance anaylyser===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Attendance")
    print("4. Attendance Report")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":

      add_student()

    elif choice == "2":

        viewstudents()
    elif choice == "3":
        calculateattendance()    
    elif choice == "4":
        attendancereport()
    elif choice == "5":
        print("Thank you for using Student Attendance Analyzer")
        break

    else:
        print("invalidchoice")
    