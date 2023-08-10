class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print(f"Task {index} updated.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.show_tasks()
        elif choice == "3":
            index = int(input("Enter task index to update: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
        elif choice == "4":
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
