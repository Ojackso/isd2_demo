from student.student import Student
from department.department import Department
from course import *

def main():
    # Given students populated into a list.
    students = []
    student_number = 1000
    for i in range(10):
        name = "Student" + str(i)
        student_number += 1 
        try:
            student = Student(student_number, name, Department.COMPUTER_SCIENCE )
            students.append(student)
        except ValueError as e:
            print(e)
    
    #1. Create an instance of the Course class with valid inputs.
    # If an exception occurs, print the exception instance.
    # Comment out once tested.
    # try:
    #     software_development_fundamentals = Course("SDF", Department.COMPUTER_SCIENCE, 6)
    # except ValueError as e:
    #     print(e)
    
    #2. Define a Lecture Course with a capacity of 20 and a current enrollment of 19
    # Use any valid values for the other parameters.
    # print the object
    try:
        isd = LectureCourse("ISD", Department.COMPUTER_SCIENCE,6,20,19,"P414")
        print(isd)
    except ValueError as e:
        print(e)


    #3. Define a Lab Course with a capacity of 20 and a current enrollment of 8
    # Use any valid values for the other parameters.
    # print the object.
    try:
        chemistry = LabCourse("Chemistry", Department.COMPUTER_SCIENCE, 6,20,8, "Googles")
        print(chemistry)
    except ValueError as e:
        print(e)



    #4. Using a loop, enroll the students from the students list above
    # into the lecture course defined above.  Print the message returned
    # from the enroll_student method.
    for student in students:
        print(chemistry.enroll_student(student))



    #5. Using a loop, enroll the students from the students list above
    # into the lab course defined above.  Print hte message returned from 
    # the enroll_student method.




if __name__ == "__main__":
    main()
    
    
    