import json
from datetime import datetime, timedelta

# File to store tasks
TASK_FILE = 'tasks.json'

# Load tasks from file if it exists
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD, optional): ")
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Task not added.")
            return
    tasks.append({
        "description": description,
        "due_date": due_date if due_date else None,
        "status": "Pending"
    })
    save_tasks(tasks)
    print("Task added successfully!")

# View tasks (all, completed, pending, due soon)
def view_tasks(tasks):
    print("\nView options:")
    print("1. All tasks")
    print("2. Completed tasks")
    print("3. Pending tasks")
    print("4. Tasks due soon (within 3 days)")
    
    option = input("Choose an option: ")
    
    today = datetime.today()
    
    if option == '1':
        filtered_tasks = tasks
    elif option == '2':
        filtered_tasks = [task for task in tasks if task['status'] == 'Completed']
    elif option == '3':
        filtered_tasks = [task for task in tasks if task['status'] == 'Pending']
    elif option == '4':
        filtered_tasks = [
            task for task in tasks
            if task['due_date'] and datetime.strptime(task['due_date'], "%Y-%m-%d") <= today + timedelta(days=3)
        ]
    else:
        print("Invalid option.")
        return
    
    if not filtered_tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(filtered_tasks, 1):
            due_date = task['due_date'] if task['due_date'] else "No due date"
            print(f"{idx}. {task['description']} | Due: {due_date} | Status: {task['status']}")
    print()

# Mark task as completed
def mark_task_complete(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['status'] = 'Completed'
        save_tasks(tasks)
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

# Edit task
def edit_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to edit: ")) - 1
    if 0 <= task_num < len(tasks):
        new_description = input("Enter new task description: ")
        new_due_date = input("Enter new due date (YYYY-MM-DD, optional): ")
        if new_due_date:
            try:
                datetime.strptime(new_due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format.")
                return
        tasks[task_num]['description'] = new_description
        tasks[task_num]['due_date'] = new_due_date if new_due_date else None
        save_tasks(tasks)
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        del tasks[task_num]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

# User menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
