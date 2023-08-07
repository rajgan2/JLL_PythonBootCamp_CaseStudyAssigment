class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty.")

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid index.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nChoose Below Tasks:")
        print("1. Enter 1 To Add Task")
        print("2. Enter 2 To View Tasks")
        print("3. Enter 3 To Update Task")
        print("4. Enter 4 To Delete Task")
        print("5. Enter 5 To Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == 2:
            todo_list.view_tasks()
        elif choice == 3:
            index = int(input("Enter the index of the task to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == 4:
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index)
        elif choice == 5:
            print("Exited.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()