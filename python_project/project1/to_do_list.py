import json
import os

# File to store student data
FILE = "students.json"

# Load data from file
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

# Save data to file
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add new student
def add_student(data):
    roll = input("Enter Roll Number: ")
    if roll in data:
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    marks = {}
    subjects = int(input("How many subjects? "))
    for _ in range(subjects):
        sub = input("Enter subject name: ")
        score = float(input(f"Enter marks for {sub}: "))
        marks[sub] = score
    data[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")

# Display all students
def display_students(data):
    if not data:
        print("No student records found.")
        return
    for roll, details in data.items():
        print(f"\nRoll: {roll}, Name: {details['name']}")
        for sub, score in details['marks'].items():
            print(f"   {sub}: {score}")
        avg = sum(details['marks'].values()) / len(details['marks'])
        print(f"   Average: {avg:.2f}")

# Search student by roll
def search_student(data):
    roll = input("Enter Roll Number to search: ")
    if roll in data:
        details = data[roll]
        print(f"Roll: {roll}, Name: {details['name']}")
        for sub, score in details['marks'].items():
            print(f"   {sub}: {score}")
    else:
        print("Student not found!")

# Update student record
def update_student(data):
    roll = input("Enter Roll Number to update: ")
    if roll in data:
        print("1. Update Name")
        print("2. Update Marks")
        choice = input("Enter choice: ")
        if choice == "1":
            new_name = input("Enter new name: ")
            data[roll]["name"] = new_name
            print("Name updated successfully!")
        elif choice == "2":
            sub = input("Enter subject name: ")
            if sub in data[roll]["marks"]:
                new_marks = float(input("Enter new marks: "))
                data[roll]["marks"][sub] = new_marks
                print("Marks updated successfully!")
            else:
                print("Subject not found!")
    else:
        print("Student not found!")

# Delete student
def delete_student(data):
    roll = input("Enter Roll Number to delete: ")
    if roll in data:
        del data[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

# Main Program
def main():
    data = load_data()
    while True:
        print("\n===== Student Grade Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            display_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            update_student(data)
        elif choice == "5":
            delete_student(data)
        elif choice == "6":
            save_data(data)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
