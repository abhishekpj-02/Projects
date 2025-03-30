gradebook = {}

def add_student():
    name = input("Enter student name: ")
    if name in gradebook:
        print(f"Student '{name}' already exists with grade {gradebook[name]}.")
    else:
        try:
            grade = float(input(f"Enter grade for {name}: "))
            gradebook[name] = grade
            print(f"Student '{name}' added with grade {grade}.")
        except ValueError:
            print("Invalid grade. Please enter a number.")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in gradebook:
        del gradebook[name]
        print(f"Student '{name}' removed.")
    else:
        print(f"Student '{name}' does not exist.")

def update_grade():
    name = input("Enter student name: ")
    if name in gradebook:
        try:
            grade = float(input(f"Enter new grade for {name}: "))
            gradebook[name] = grade
            print(f"Updated grade for '{name}' to {grade}.")
        except ValueError:
            print("Invalid grade. Please enter a number.")
    else:
        print(f"Student '{name}' does not exist.")

def calculate_average():
    if gradebook:
        avg = sum(gradebook.values()) / len(gradebook)
        print(f"Average grade: {avg:.2f}.")
    else:
        print("No students in the gradebook.")

def display_students():
    if gradebook:
        print("\nStudent Grades:")
        for name, grade in gradebook.items():
            print(f"- {name}: {grade}")
    else:
        print("No students in the gradebook.")

while True:
    print("\nGradebook Menu:")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Grade")
    print("4. Calculate Average")
    print("5. Display Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        update_grade()
    elif choice == "4":
        calculate_average()
    elif choice == "5":
        display_students()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
