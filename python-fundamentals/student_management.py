class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll: {self.roll}, Name: {self.name}, Marks: {self.marks}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}  # DSA: Dictionary for O(1) access by roll
        self.history = []   # DSA: Stack to undo last action

    def add_student(self):
        roll = input("Enter roll number: ").strip()
        if roll in self.students:
            print("Student with this roll number already exists.")
            return
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        self.students[roll] = Student(roll, name, marks)
        self.history.append(('add', roll))
        print(f"Student {name} added successfully.")

    def remove_student(self):
        roll = input("Enter roll number to remove: ").strip()
        if roll in self.students:
            removed = self.students.pop(roll)
            self.history.append(('remove', roll, removed))
            print(f"Student {removed.name} removed.")
        else:
            print("Student not found.")

    def update_student(self):
        roll = input("Enter roll number to update: ").strip()
        if roll in self.students:
            old_data = self.students[roll]
            name = input("Enter new name: ")
            marks = float(input("Enter new marks: "))
            self.students[roll] = Student(roll, name, marks)
            self.history.append(('update', roll, old_data))
            print("Student record updated.")
        else:
            print("Student not found.")

    def search_student(self):
        roll = input("Enter roll number to search: ").strip()
        if roll in self.students:
            print(self.students[roll])
        else:
            print("Student not found.")

    def view_all_students(self):
        if not self.students:
            print("No student records available.")
            return
        print("\n--- Student Records ---")
        for student in self.students.values():
            print(student)

    def undo_last_action(self):
        if not self.history:
            print("No actions to undo.")
            return

        last = self.history.pop()
        action = last[0]

        if action == 'add':
            roll = last[1]
            if roll in self.students:
                del self.students[roll]
                print(f"Undo: Added student with roll {roll} removed.")
        elif action == 'remove':
            roll, student = last[1], last[2]
            self.students[roll] = student
            print(f"Undo: Removed student {student.name} restored.")
        elif action == 'update':
            roll, old_student = last[1], last[2]
            self.students[roll] = old_student
            print(f"Undo: Student {roll} reverted to previous data.")

    def menu(self):
        while True:
            print("\n--- Student Management ---")
            print("1. Add Student\n2. Remove Student\n3. Update Student\n4. Search Student\n5. View All")
            print("6. Undo Last Action\n7. Exit")
            choice = input("Choose (1-7): ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.search_student()
            elif choice == "5":
                self.view_all_students()
            elif choice == "6":
                self.undo_last_action()
            elif choice == "7":
                print("Exiting Student Management System.")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.menu()
