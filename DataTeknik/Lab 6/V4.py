import integer_input

class Student:
    def __init__(self, id_number, first_name, last_name):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, ID Number: {self.id_number}"

    def edit_info(self):
        print(f"Current information for the student:")
        print(str(self))
        self.first_name = input("Enter the new first name: ")
        self.last_name = input("Enter the new last name: ")
        self.id_number = input("Enter the new ID number: ")
        print("Student information has been edited.")

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def search_student_by_id(self, id_number_to_find):
        for student in self.students:
            if student.id_number == id_number_to_find:
                return student
        return None  # Return None if the student is not found

def load_student_data(school, filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

            # Process data from the file in sets of three lines
            for i in range(0, len(lines), 3):
                id_number = lines[i].strip()
                last_name = lines[i + 1].strip()
                first_name = lines[i + 2].strip()

                # Create an instance of the Student class and add it to the school list
                student = Student(id_number, first_name, last_name)
                school.add_student(student)

            print("Student information has been loaded from the file.")
    except FileNotFoundError:
        print("No previously saved student information was found.")

def edit_student(student_list, id_number_to_edit):
    for student in student_list:
        if student.id_number == id_number_to_edit:
            student.edit_info()
            return

    print("The student with the specified ID number is not part of the student list.")

def delete_student(student_list, id_number_to_delete):
    for student in student_list:
        if student.id_number == id_number_to_delete:
            student_list.remove(student)
            print("Student information has been deleted.")
            return

    print("The student with the specified ID number is not part of the student list.")

def search_student_by_id(student_list, id_number_to_search):
    for student in student_list:
        if student.id_number == id_number_to_search:
            return student

    return None

school = School()

while True:
    print("Choose an option:")
    print("1. Import student information from a file")
    print("2. Add students manually")
    print("3. Edit student information")
    print("4. Delete student information")
    print("5. Finish")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        filepath = input("Enter the file path: ")
        load_student_data(school, filepath)

    elif choice == '2':
        num_students = integer_input.get_integer_input("How many students' information do you want to add? ")

        with open("students.txt", 'a') as file:
            for i in range(num_students):
                first_name = input(f"Enter student {i + 1}'s first name: ")
                last_name = input(f"Enter student {i + 1}'s last name: ")
                id_number = input(f"Enter student {i + 1}'s ID number: ")

                student = Student(id_number, first_name, last_name)
                school.add_student(student)

                file.write(student.id_number + "\n")
                file.write(student.last_name + "\n")
                file.write(student.first_name + "\n")

                print("Student information has been added.")

    elif choice == '3':
        id_number_to_edit = input("Enter the ID number of the student you want to edit: ")
        edit_student(school.students, id_number_to_edit)

    elif choice == '4':
        id_number_to_delete = input("Enter the ID number of the student you want to delete: ")
        delete_student(school.students, id_number_to_delete)

    elif choice == '5':
        print("The program is ending.")
        break

    else:
        print("Invalid choice. Enter 1, 2, 3, 4, or 5.")

list_input = input("Do you want to search for students in the list? Yes (y) No (n): ")

while list_input.lower() == 'y':
    search_id = input("Enter the ID number of the student you are looking for: ")
    found_student = search_student_by_id(school.students, search_id)

    if found_student:
        print("Student found:")
        print(str(found_student))
    else:
        print("The student with the specified ID number is not part of the student list.")

    list_input = input("Do you want to search for more students? Yes (y) No (n): ")

if list_input.lower() == 'n':
    print("Student list:")
    for student in school.students:
        print(str(student))
else:
    print("Invalid choice, program ending.")
