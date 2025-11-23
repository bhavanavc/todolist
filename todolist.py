def display_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as done")
    print("4. Exit")
    print("5. Erase all tasks")

def main():
    tasks = [] #list of tuples: (task_string, status)

    while True:
        display_menu()
        choice=  input("Enter your choice").strip()

        if choice == '1':
            task = input("Enter task:").strip()
            tasks.append((task, "Pending"))
            print("Task added!")

        elif choice =='2':
            if not tasks:
                print("No tasks to show")
            else:
                for i, (task, status) in enumerate(tasks, 1):
                    print(f"{i}. {task} - {status}")

        elif choice =='3' :
            if not tasks:
                print("No tasks to mark as done")
            else:
                for i, (task, status) in enumerate(tasks,1):
                    print(f"{i}. {task} - {status}")
                try:
                    idx = int(input("Enter task number to mark as done"))
                    if 1<= idx <= len(tasks):
                        task, _ = tasks[idx - 1] 
                        tasks[idx - 1] = (task, "Done")
                        print(f"Marked \"{task}\" as done")
                    else:
                        print("Invalid number")
                except ValueError:
                    print("Please enter a valid number")

        elif choice == '4':
            confirm = input("Are you sure you want to erase all the tasks? (yes/no):").strip().lower()
            if confirm == 'yes':
                tasks.clear()
                print("All tasks erased!")
            else:
                print("Erase cancelled.")

        else:
            print("invalid choice. Try again")

if __name__ == "__main__":
    main()                        
                              