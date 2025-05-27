import os
import json

TASKS_FILE = "tasks.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

clear_screen()
def main():
    tasks = load_tasks()

    def showTasks():
        print("\nTasks:")
        for index, task in enumerate(tasks):
            status = "[✅]" if task["done"] else "[❌]"
            print(f"{index + 1}. {task['task']} - {status}")

    while True:
        print("\n==== To-Do List ====")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. EXit")

        choice = input("Enter your chouce: ")

        if choice == '1':
            print()
            clear_screen()

            while True:
                print("Enter how many tasks you want, return null to stop")
                task = input("Enter a task: ")
                if task:
                    tasks.append({"task": task, "done": False})
                    print("Task added!")
                else:
                    clear_screen()
                    showTasks()
                    break
            save_tasks(tasks)

        elif choice == '2':
            clear_screen()
            showTasks()

        elif choice == '3':
            clear_screen()
            showTasks()
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = not tasks[task_index]["done"]
                status = "done" if tasks[task_index]["done"] else "undone"
                print(f"Task '{tasks[task_index]['task']}' marked as {status}!")
            else:
                print("Invalid task number.")
            save_tasks(tasks)
            clear_screen()
            showTasks()


        elif choice =='4':
            clear_screen()
            print("[d] - removes all tasks marked as done | select with index number [1-9]")
            showTasks()
            
            task_index = input("Enter the task number to remove: ")
            if task_index.lower() == 'd':
                tasks = [task for task in tasks if not task["done"]]
                
            else:
                removed_task = tasks.pop(int(task_index)-1)
            save_tasks(tasks)
            clear_screen()
            showTasks()
                

        elif choice == '5':
            print("Exiting the To-Do List.")
            break

        else:
            clear_screen()
            print("Invalid choice. Please try again.")
            showTasks()
    

if __name__ == "__main__":
    main()