tasks = []
def add_task():
    while True:
        task = input("Enter task: (Type 'done' to return to main menu)").strip()
        if task.lower() == "done":
                print("Returning to main menu...\n")
                break
        if task:
                tasks.append(task)
                print("Task added successfully!✅\n")
        else:
            print("Task can't be empty.❎\n")
            
def view_task():
    if len(tasks)==0:
            print("No tasks found.\n")
    else:
        print("===== Your tasks =====")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")
            print()

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add task")
    print("2. View task")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue
    
    if choice == 1:
        add_task()

    elif choice == 2:
        view_task()

    elif choice == 3:
        print("Thanks for using.")
        break
    else :
        print("Invalid choice.")
    
