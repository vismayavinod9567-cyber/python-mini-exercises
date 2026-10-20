class College:
    def __init__(self):
        self.college_name=""
        self.place=""
        self.mobile=""
    def college_data(self):
        print("PLEASE ENTER THE FOLLOWING DETAILS")
        self.college_name=input("Enter your college name")
        self.place=input("Enter your college location")
        self.mobile=input("Enter your college mobile")
    def college_details(self):
        print("******COLLEGE DETAILS****")
        print("college name",self.college_name)
        print("college location",self.place)
        print("college number",self.mobile)
class Department(College):
    def __init__(self):
        self.dept_id = ""
        self.dept_name = ""
        self.hod = ""

    def dept_data(self):
        print("PLEASE ENTER THE FOLLOWING DETAILS")
        self.dept_id = input("Enter your department id ")
        self.dept_name = input("Enter your dept name")
        self.hod = input("Enter your hod name")

    def dept_details(self):
        print("******DEPARTMENT DETAILS****")
        print("Department id", self.dept_id)
        print("Department name", self.dept_name)
        print("HOD", self.hod)


class Student(Department):
    def __init__(self):
        self.sname= ""
        self.splace = ""

    def student_data(self):
        print("PLEASE ENTER THE STUDENT DETAILS")
        self.sname = input("Enter student name")
        self.splace = input("Enter student place ")
    def student_details(self):
        print("******STUDENT DETAILS****")
        print("Student name", self.sname)
        print("Place",self.splace)

obj=Student()
obj.college_data()
obj.dept_data()
obj.student_data()
obj.college_details()
obj.dept_details()
obj.student_details()
