import json
from datetime import datetime, timedelta

# File to store tasks
TASK_FILE = 'tasks.json'

# Load tasks from file if it exists, else return an empty list
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)  # Load and return task data from JSON file
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist

# Save tasks to the file, overwriting the current content
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)  # Save the tasks list in a readable JSON format

# Add a new task to the list
def add_task(tasks):
    # Get task details from user input
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD, optional): ")

    # Validate the date format if the user provides a due date
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Task not added.")
            return

    # Append new task as a dictionary with description, due date, and status
    tasks.append({
        "description": description,
        "due_date": due_date if due_date else None,  # Due date can be optional
        "status": "Pending"  # Default status is 'Pending'
    })
    save_tasks(tasks)  # Save the updated task list to the file
    print("Task added successfully!")

# View tasks based on user's choice (all, completed, pending, due soon)
def view_tasks(tasks):
    print("\nView options:")
    print("1. All tasks")
    print("2. Completed tasks")
    print("3. Pending tasks")
    print("4. Tasks due soon (within 3 days)")
    
    # Get user's choice for viewing tasks
    option = input("Choose an option: ")
    
    # Get current date to compare for 'due soon' tasks
    today = datetime.today()
    
    # Filter tasks based on user's selection
    if option == '1':
        filtered_tasks = tasks  # View all tasks
    elif option == '2':
        filtered_tasks = [task for task in tasks if task['status'] == 'Completed']  # Only completed tasks
    elif option == '3':
        filtered_tasks = [task for task in tasks if task['status'] == 'Pending']  # Only pending tasks
    elif option == '4':
        # Tasks due within the next 3 days
        filtered_tasks = [
            task for task in tasks
            if task['due_date'] and datetime.strptime(task['due_date'], "%Y-%m-%d") <= today + timedelta(days=3)
        ]
    else:
        print("Invalid option.")  # Handle invalid input
        return
    
    # Display filtered tasks or show a message if no tasks found
    if not filtered_tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(filtered_tasks, 1):
            due_date = task['due_date'] if task['due_date'] else "No due date"  # Display 'No due date' if it's None
            print(f"{idx}. {task['description']} | Due: {due_date} | Status: {task['status']}")  # Display task details
    print()

# Mark a specific task as complete
def mark_task_complete(tasks):
    view_tasks(tasks)  # First, show all tasks
    task_num = int(input("Enter task number to mark as complete: ")) - 1  # Get the task number from the user
    if 0 <= task_num < len(tasks):  # Ensure task number is valid
        tasks[task_num]['status'] = 'Completed'  # Update status to 'Completed'
        save_tasks(tasks)  # Save the updated tasks to the file
        print("Task marked as complete.")
    else:
        print("Invalid task number.")  # Handle invalid task number

# Edit the description or due date of a specific task
def edit_task(tasks):
    view_tasks(tasks)  # First, show all tasks
    task_num = int(input("Enter task number to edit: ")) - 1  # Get task number from the user
    if 0 <= task_num < len(tasks):  # Ensure task number is valid
        # Get new task details from the user
        new_description = input("Enter new task description: ")
        new_due_date = input("Enter new due date (YYYY-MM-DD, optional): ")

        # Validate the new due date if provided
        if new_due_date:
            try:
                datetime.strptime(new_due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format.")
                return

        # Update task details
        tasks[task_num]['description'] = new_description
        tasks[task_num]['due_date'] = new_due_date if new_due_date else None
        save_tasks(tasks)  # Save updated tasks
        print("Task updated successfully.")
    else:
        print("Invalid task number.")  # Handle invalid task number

# Delete a specific task
def delete_task(tasks):
    view_tasks(tasks)  # First, show all tasks
    task_num = int(input("Enter task number to delete: ")) - 1  # Get task number from the user
    if 0 <= task_num < len(tasks):  # Ensure task number is valid
        del tasks[task_num]  # Remove the task from the list
        save_tasks(tasks)  # Save updated task list
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")  # Handle invalid task number

# Main user menu that offers various options to manage tasks
def main():
    tasks = load_tasks()  # Load tasks from file on program start
    
    # Loop to keep showing the menu until the user decides to exit
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")
        
        # Get user choice for the menu
        choice = input("Enter your choice: ")
        
        # Call corresponding function based on user's choice
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
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choice

# Start the program
if __name__ == "__main__":
    main()  # Call the main function to start the program
