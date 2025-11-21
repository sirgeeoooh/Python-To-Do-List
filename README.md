# Task Manager CLI

A simple and efficient Command Line Interface (CLI) task management application built with Python. This program helps you manage your daily tasks through an intuitive text-based interface.

## Features

- ✅ **Add Tasks** - Create new tasks with input validation
- ✅ **View Tasks** - Display all current tasks in a numbered list
- ✅ **Delete Tasks** - Remove tasks by their number
- ✅ **Quit Application** - Clean exit from the program
- ✅ **Input Validation** - Comprehensive error handling for invalid inputs
- ✅ **User-Friendly Interface** - Clear menus and visual separators

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/task-manager-cli.git
Navigate to the project directory:

bash
cd task-manager-cli
Usage
Run the application:

bash
python todo-list.py
Follow the menu prompts:

Press 1 to add a new task

Press 2 to view all tasks

Press 3 to delete a task

Press 4 to quit the application

Example Session
text
=== WELCOME TO TASK MANAGER ===
Manage your task efficiently!


=== TASK MANAGER ===
1. Add Task
2. View Task
3. Delete Task
4. Quit
Enter your choice (1-4): 1
==================================================
Enter task: Buy groceries
Task Buy groceries added!
==================================================
Error Handling
The application includes robust error handling for:

❌ Invalid menu choices (only 1-4 accepted)

❌ Empty task inputs

❌ Non-numeric inputs when deleting tasks

❌ Attempting to delete non-existent tasks

❌ Viewing tasks when none exist

Project Structure
text
task-manager-cli/
│
├── todo-list.py          # Main application file
├── README.md             # Project documentation
└── .gitignore           # Git ignore file (if any)
Key Components
Main Classes:

InputOptions - Handles menu input validation

QuitProgram - Manages application state

NotValidInput - Custom exception class

Core Functions:

add_task() - Adds new tasks with validation

view_task() - Displays all tasks

delete_task() - Removes tasks with error handling

display_menu() - Shows the main menu

welcome_message() - Displays welcome banner

Code Quality Features
🏗️ Object-oriented design with custom classes

🛡️ Comprehensive error handling with try/except/else/finally

📝 Detailed docstrings and comments

🔄 Input validation at every step

👥 User-friendly error messages

Testing
The application has been tested against various edge cases:

Empty task lists

Invalid user inputs

Boundary conditions for task numbers

Special characters in task descriptions

To test the application:

Run the program

Try adding empty tasks

Attempt to delete from empty list

Enter invalid menu options

Test task numbering boundaries

Contributing
Feel free to fork this project and submit pull requests for any improvements. Some potential enhancements:

Task prioritization

Due dates for tasks

Task categories

Persistent storage (file/database)

Task editing functionality

License
This project is open source and available under the MIT License.

Author
Created as a learning project for Python CLI application development.
