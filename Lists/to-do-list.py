to_do_list = []

while True:
    print("To-Do List:")
    for index, item in enumerate(to_do_list, 1):
        print(f"{index}. {item}")
    
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter a new task: ")
        to_do_list.append(task)
    elif choice == '2':
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(to_do_list):
            removed_task = to_do_list.pop(task_index)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number.")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
