# app.py

from todo import Todo

def main():
    todo_list = Todo()
    print("Simple To-Do List App")
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter a task: ")
            try:
                result = todo_list.add_task(task)
                print(result)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            tasks = todo_list.get_tasks()
            if tasks:
                print("Your tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks found.")
        elif choice == "3":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
