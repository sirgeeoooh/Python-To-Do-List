"""
Task Manager CLI

A simple command-line application for managing daily tasks.
Features: Add, view, delete tasks with full error handling.

Run directly: python todo-list.py
"""

# ===== IMPORTS =====
# (None needed for this project)

# ===== CONSTANTS =====
MENU_CHOICES = ['1', '2', '3', '4']

# ===== EXCEPTION CLASSES =====
class TaskManagerError(Exception):
    """Base exception class for all Task Manager errors"""
    pass

class NotValidInput(TaskManagerError):
    pass

class TaskAlreadyInListError(TaskManagerError):
    pass

class NoTasksError(TaskManagerError):
    pass

class TaskMinimumCharError(TaskManagerError):
    pass

# ===== REGULAR CLASSES =====
class InputOptions:
    @staticmethod
    def validate_choice(choice):
        if choice not in MENU_CHOICES:
            raise NotValidInput('Input must be between (1-4)')
        return choice

class QuitProgram:
    def __init__(self):
        self.quit_program = False
        
    def set_quit(self, value):
        self.quit_program = value
        
    def should_quit(self):
        return self.quit_program

def display_menu():
    print('\n=== TASK MANAGER ===')
    print('1. Add Task')
    print('2. View Task')
    print('3. Delete Task')
    print('4. Quit')
    
def welcome_message():
    print('=== WELCOME TO TASK MANAGER ===')
    print('Manage your task efficiently!\n')

def add_task(tasks):
    """
    Add a new task to the task list after validating it's not empty and not in the list already.
    
    Add multiple tasks continuously until user enters empty input.
    
    Args:
        tasks (list): The list of tasks to add to
    """
    print("\n=== Add Task (press Enter when done) ===")
    while True:
        try:
            task = input('\nEnter task (or press Enter to finish): ').strip()
            task_lower = task.casefold()
            
            if not task:
                print('\nFinished adding tasks.')
                break
            
            if len(task) < 3:
                raise TaskMinimumCharError("Task must be at least 3 characters long")
            
            if task_lower in [t.casefold() for t in tasks]:
                raise TaskAlreadyInListError("Task already in the list, enter new task or return to main menu.")
            
            tasks.append(task)
            print(f"Task '{task}' added!")
            print('=' * 50)  
            
        except TaskMinimumCharError as e:
            print(f'\nError: {e}')
            
        except TaskAlreadyInListError as e:
            print(f'\nError: {e}')
    
def view_task(tasks):
    try:
        if not tasks:
            raise NoTasksError("No tasks to display!")
        
        print('=== ALL TASK TO BE COMPLETED ===')
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    
    except NoTasksError as e:
        print(f'\nError: {e}')
        
            
def delete_task(tasks):
    """
    Delete tasks by its number with error handling for empty list and task number validation.
    
    Args:
        tasks (list): The list of tasks to delete from
    """
    
    while True:
        try:
            if not tasks:
                raise NoTasksError("No tasks to display!")
        
            view_task(tasks)
            
            delete_input = input('Input the task number to delete (or press Enter to Return to Main Menu): ').strip()
            
            if not delete_input:
                print('Finished deleting tasks.')
                break
            
            delete_input = int(delete_input)
            
            if delete_input < 1 or delete_input > len(tasks):
                raise IndexError("Task doesn't exist!")
            
            removed_task = tasks.pop(delete_input - 1)
            print(f"Task '{removed_task}' deleted!\n")
            
            continue
        
        except NoTasksError as e:
            print(f'\nError: {e}')
        
        except IndexError as e:
            print(f'\nError: {e}')

def main():
    tasks = []
    quit_controller = QuitProgram()
    welcome_message()

    while not quit_controller.should_quit():
        display_menu()
        choice = input('Enter your choice (1-4): ')
        print('=' * 50) 

        try:
            InputOptions.validate_choice(choice)
            
            if choice == '1':
                add_task(tasks)
            
            elif choice =='2':
                view_task(tasks)
            
            elif choice =='3':
                delete_task(tasks)
            
            elif choice =='4':
                quit_controller.set_quit(True)
                
            print('=' * 50) 
            
        except NotValidInput as e:
            print(f'Error: {e}')
            print('=' * 50)                    
                    
if __name__ == '__main__':
    main()