# Task Manager CLI

A simple and efficient Command Line Interface (CLI) task management application built with Python. This program helps you manage your daily tasks through an intuitive text-based interface with comprehensive error handling.

## Features

- ✅ **Add Tasks** - Create new tasks with input validation (minimum 3 characters, no duplicates)
- ✅ **View Tasks** - Display all current tasks in a numbered list
- ✅ **Delete Tasks** - Remove tasks by their number with continuous deletion support
- ✅ **Quit Application** - Clean exit from the program
- ✅ **Input Validation** - Comprehensive error handling for invalid inputs
- ✅ **User-Friendly Interface** - Clear menus and visual separators
- ✅ **Case-Insensitive Detection** - Prevents duplicate tasks regardless of capitalization
- ✅ **Batch Operations** - Add or delete multiple tasks in one session

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone this repository:

```bash
git clone https://github.com/sirgeeoooh/Python-To-Do-List.git
Navigate to the project directory:

bash
cd task-manager-cli
Usage
Run the application:

bash
python todo-list.py
Follow the menu prompts:

Press 1 to add new tasks (press Enter when done)

Press 2 to view all tasks

Press 3 to delete tasks (press Enter when done)

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

=== Add Task (press Enter when done) ===

Enter task (or press Enter to finish): Buy groceries
Task 'Buy groceries' added!
==================================================

Enter task (or press Enter to finish):
Finished adding tasks.
Error Handling
The application includes robust error handling for:

❌ Invalid menu choices (only 1-4 accepted)

❌ Empty task inputs

❌ Tasks shorter than 3 characters

❌ Duplicate tasks (case-insensitive detection)

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
Code Architecture
Exception Classes:

TaskManagerError - Base exception class

NotValidInput - Invalid menu input

TaskAlreadyInListError - Duplicate task detection

NoTasksError - Empty task list operations

TaskMinimumCharError - Task too short validation

Core Classes:

InputOptions - Handles menu input validation

QuitProgram - Manages application state

Main Functions:

add_task() - Adds new tasks with duplicate prevention

view_task() - Displays all tasks with numbered list

delete_task() - Removes tasks with continuous operation support

display_menu() - Shows the main menu interface

welcome_message() - Displays welcome banner

Code Quality Features
🏗️ Object-oriented design with custom exception hierarchy

🛡️ Comprehensive error handling with try/except blocks

📝 Detailed docstrings and code documentation

🔄 Input validation at every user interaction point

👥 User-friendly error messages with clear instructions

🎯 Case-insensitive duplicate detection for better UX

🔄 Batch operations for efficient task management

Testing
The application has been tested against various edge cases:

Empty task lists and operations

Invalid user inputs (non-numbers, out-of-range values)

Duplicate task prevention with different capitalizations

Minimum character requirements (3 characters)

Boundary conditions for task numbers

Continuous add/delete operations

To test the application:

Run the program

Try adding empty tasks or tasks shorter than 3 characters

Attempt to add duplicate tasks with different capitalizations

Delete from empty list

Enter invalid menu options

Test continuous add/delete functionality

Contributing
Feel free to fork this project and submit pull requests for any improvements. Some potential enhancements:

Task prioritization system

Due dates for tasks

Task categories or tags

Persistent storage (JSON file/database)

Task editing functionality

Task completion status

Search and filter tasks

Export tasks to file

License
This project is open source and available under the MIT License.

Author
Created as a learning project for Python CLI application development, demonstrating object-oriented programming, error handling, and user interface design.
```
