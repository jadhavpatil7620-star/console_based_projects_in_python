# class Student:
#     def __init__(self,sid,name,marks):
#         self.sid=sid
#         self.name=name
#         self.marks=marks
#     def calculate_grade(self):
#         if self.marks>=90:
#             return "A"
#         elif self.marks>=75:
#             return "B"
#         elif self.marks>=50:
#             return "C"
#         elif self.marks>=35:
#             return "D"
#         else:
#             return "Fail."
        
# class StudentManager:
#     def __init__(self):
#         self.students=[]
        
#     def add_students(self):
#         sid=int(input("Enter student ID: "))
#         for student in self.students:
#             if student.sid==sid:
#                 print("This ID already exits.\n")
#                 return
#         name=input("Enter student name: ")
#         marks=int(input("Enter student marks: "))
#         self.students.append(Student(sid,name,marks))
#         print("Student added successfully.\n")
        
#     def search_student_by_id(self,search_id):
#         for student in self.students:
#             if student.sid==search_id:
#                 print(f"Student ID: {student.sid}")
#                 print(f"Student Name: {student.name}")
#                 print(f"Student Marks: {student.marks}")
#                 print(f"Student Grade: {student.calculate_grade()}\n")
#                 return student
#         print("Student not found.")
#         return None
    
#     def update_student_deatils(self):
#         sid=int(input("Enter student ID to update: "))
#         student=self.search_student_by_id(sid)
#         if student:
#             student.name=input("Enter new name: ")
#             student.marks=int(input("Enter new marks: "))
#             print("Student update successfully.\n")
            
#     def delete_student(self):
#         sid=int(input("Enter student ID to delete: "))
#         for i,student in enumerate(self.students):
#             if student.sid==sid:
#                 del self.students[i]
#                 print("Student deleted successfully.\n")
#                 break
#                 return
#             print("Student not found.\n")

# manager=StudentManager()
# while True:
#     print("1. Add Student")
#     print("2. Search Student by ID")
#     print("3. Update Student deatils")
#     print("4. Delete student")
#     print("5. Exit")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         manager.add_students()
#     elif choice==2:
#         search_id=int(input("Enter student ID to search: "))
#         manager.search_student_by_id(search_id)
#     elif choice==3:
#         manager.update_student_deatils()
#     elif choice==4:
#         manager.delete_student()
#     elif choice==5:
#         print("Exiting the program.")
#         break
#     else:
#         print("Invalid choice. Please try again.\n")


students=[]
courses=set()

def add_student():
    sid=int(input("Enter student ID: "))
    for student in students:
        if student['basic_info'][0]==sid:
            print("Student ID already exitis.\n")
            return
    name=input("Enter student name: ")
    age=int(input("Enter student age: "))
    course=input("Enter course name: ")
    
    basic_info=(sid,name)
    
    student={
        'basic_info':basic_info,
        'age':age,
        'course':course
    }
    
    students.append(student)
    courses.add(course)
    print("Student added successfully.\n")
    
def view_student():
    if not students:
        print("No students available.\n")
        return
    for student in students:
        print(f"Student ID:",student["basic_info"][0])
        print(f"Student Name: {student['basic_info'][1]}")
        print(f"Student age: {student['age']}")
        print(f"Student course: {student['course']}")
        
def delete_student():
    sid=int(input("Enter student ID to delete student details: "))
    for student in students:
        if student['basic_info'][0]==sid:
            students.remove(student)
            print("student details deleted successfully.\n")
            return
        print("student ID not found. Please try again.\n")
            
    sid=int(input("Enter student ID to view details: "))
    for student in students:
        if student['basic_info'][0]==sid:
            print(f"\nStudent ID:",student["basic_info"][0])
            print(f"Student Name: {student['basic_info'][1]}")
            print(f"Student age: {student['age']}")
            print(f"Student course: {student['course']}\n")
            return
        print("Student ID not found in details.\n")
        
def update_details():
    sid=int(input("Enter student ID to update details: "))
    for student in students:
        if student['basic_info'][0]==sid:
            name=input("Enter student new name: ")
            age=int(input("Enter student new age: "))
            course=input("Enter new course name: ")
            student['basic_info']=(sid,name)
            student['age']=(age)
            student['course']=(course)
            print("Student details updated successfully.\n")
            return
        print("student not found.\n")
        
while True:
    print("1. Add Student")
    print("2. View student")
    print("3. Delete student details")
    print("3. Update student details")
    print("0. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        delete_student()
        # print("Enter student ID to view details: \n")
        view_student()
    elif choice==3:
        update_details()
    elif choice==0:
        print("Exiting from program.\n")
        break
    else:
        print("Invalid choice. Please try again.\n")
        print("Invalid choice. Please try again.\n")

# class Student:
#     def __init__(self):
#         students=[]
#         courses=set()
#     def add_student(self):
#         sid=int(input("Enter student ID: "))
#         name=input("Enter student name: ")
#         course=input("Enter course name: ")
#         age=int(input("Enter age: "))
        
#         basic_info=(sid,name)
        
#         student={
#             'basic_info':basic_info,
#             'course':self.courses,
#             'age':age
#         }
        
#         self.students.append(student)
#         self.courses.add(course)
#         print("Student added successfully.\n")
        
#     def view_student(self):
#         for s in self.students:
#             print(f"Student ID: {s['basic_info'][0]}")
#             print(f"Student name: {s['basic_info'][1]}")
#             print(f"Course name: {s['course']}")
#             print(f"Age of student: {s['age']}")
            
# manage=Student()
# while True:
#     print("1. Add student")
#     print("2. View student")
#     print("3. Exit")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         Student.add_student()
#     elif choice==2:
#         Student.view_student()
#     elif choice==3:
#         break
#     else:
#         print("Invalid choice.\n")
