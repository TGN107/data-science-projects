import heapq
import os

class Task:
    def __init__(self, title, priority=1, completed=False):
        self.title = title
        self.priority = priority  # 1 = Low, 2 = Medium, 3 = High
        self.completed = completed

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"[{status}] {self.title} (Priority: {self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority=1):
        task = Task(title, priority)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):#use indexing to delete
            removed = self.tasks.pop(index)
            print(f"Deleted: {removed.title}")
        else:
            print("Invalid index!")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):#here too indexing used 
            self.tasks[index].completed = True
            print(f"Marked '{self.tasks[index].title}' as completed.")
        else:
            print("Invalid index!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\n--- Your Tasks ---")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def sort_by_priority(self):
        self.tasks.sort(key=lambda t: (-t.priority, t.completed))
        print("Tasks sorted by priority.")

    def save_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task.title}|{task.priority}|{task.completed}\n")
        print("Tasks saved to file.")

    def load_from_file(self, filename="tasks.txt"):
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            for line in f:
                title, priority, completed = line.strip().split("|")
                self.tasks.append(Task(title, int(priority), completed == "True"))
        print("Tasks loaded from file.")

# Driver function
def main():
    manager = TaskManager()
    manager.load_from_file()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Sort by Priority")
        print("6. Save and Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            try:
                priority = int(input("Priority (1=Low, 2=Med, 3=High): "))
                manager.add_task(title, priority)
            except ValueError:
                print("Invalid priority!")
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            try:
                idx = int(input("Enter index to delete: "))
                manager.delete_task(idx)
            except ValueError:
                print("Invalid input!")
        elif choice == "4":
            try:
                idx = int(input("Enter index to mark complete: "))
                manager.mark_completed(idx)
            except ValueError:
                print("Invalid input!")
        elif choice == "5":
            manager.sort_by_priority()
        elif choice == "6":
            manager.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
