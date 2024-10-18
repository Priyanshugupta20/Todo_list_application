# Command-Line To-Do List Manager

## Project Description
This is a Python-based **Command-Line To-Do List Manager** that allows users to manage their tasks efficiently. It lets users add, view, edit, mark as complete, and delete tasks. The tasks are saved to a JSON file to ensure persistence between program runs.

## Features
- **Add Task:** Users can add tasks with a description, due date (optional), and status.
- **View Tasks:** Users can view:
  - All tasks
  - Completed tasks
  - Pending tasks
  - Tasks due within 3 days
- **Manage Tasks:** Users can:
  - Mark tasks as completed
  - Edit task description or due date
  - Delete tasks
- **Data Persistence:** Tasks are saved to a `tasks.json` file so they are available between program runs.

## Requirements
- Python 3.x
- No external libraries required (uses built-in Python libraries: `json`, `datetime`)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-list-manager.git
