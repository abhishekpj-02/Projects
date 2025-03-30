# Initialize the gradebook as an empty dictionary
gradebook = {}

def add(name, grade):
    if name in gradebook:
        print(f"Student {name} already exists.")
    else:
        gradebook[name] = grade
        print(f"Student {name} added with grade {grade}.")

def remove(name):
    if name in gradebook:
        del gradebook[name]
        print(f"Student {name} removed.")
    else:
        print(f"Student {name} does not exist.")

def update_grade(name, grade):
    if name in gradebook:
        gradebook[name] = grade
        print(f"Grade updated for student {name} to {grade}.")
    else:
        print(f"Student {name} does not exist.")

def average():
    if gradebook:
        average = sum(gradebook.values()) / len(gradebook)
        print(f"Average grade for the class is {average:.2f}.")
        return average
    else:
        print("No students in the gradebook.")
        return None
    
def display():
    if gradebook:
        print("\nStudent Grades:")
        for name, grade in gradebook.items():
            print(f"- {name.capitalize()}: {grade}")
    else:
        print("No students in the gradebook.")

        
# Menu Loop
while True:
    print("\nGradebook Menu:")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Grade")
    print("4. Calculate Average")
    print("5. Display Students")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add()
    elif choice == "2":
        remove()
    elif choice == "3":
        update_grade()
    elif choice == "4":
        average()
    elif choice == "5":
        display()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")