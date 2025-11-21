"""
Task Manager CLI

A simple command-line application for managing daily tasks.
Features: Add, view, delete tasks with full error handling.

Run directly: python todo-list.py
"""

def display_menu():
    print('\n=== TASK MANAGER ===')
    print('1. Add Task')
    print('2. View Task')
    print('3. Delete Task')
    print('4. Quit')

def add_task(tasks):
    """
    Add a new task to the task list after validating it's not empty.
    
    Args:
        tasks (list): The list of tasks to add to
    """
    try:
        task = input('Enter task: ').strip()
        if not task:
            raise ValueError('Task cannot be empty!')
    
    except ValueError as e:
        print(f'Error: {e}')
    else:
        tasks.append(task)
        print(f'Task {task} added!')
    finally:
        print('Task cannot be empty! Please enter a task')
    
def view_task(tasks):
    if not tasks:
        print('No tasks to display')
    else:
        print('=== ALL TASK TO BE COMPLETED ===')
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            
def delete_task(tasks):
    """
    Delete a task by its number with comprehensive error handling.
    
    Args:
        tasks (list): The list of tasks to delete from
    """
    try:
        if not tasks:
            print('There are no task to delete.')
            return
        
        view_task(tasks)
        delete_input = int(input('Input the task number to delete: '))
        
        if delete_input < 1 or delete_input > len(tasks):
            raise IndexError("Task doesn't exist!")
        
    except ValueError:
        print('Please enter a valid number!')
    
    except IndexError as e:
        print(f'Error: {e}')
    else:
        removed_task = tasks.pop(delete_input - 1)
        print(f'Task {removed_task} deleted!')
    finally:
        print('Delete operation completed!')

def welcome_message():
    print('=== WELCOME TO TASK MANAGER ===')
    print('Manage your task efficiently!\n')
    
class NotValidInput(Exception):
    pass

class InputOptions:
    MENU_CHOICES = ['1','2','3','4']
    
    @staticmethod
    def validate_choice(choice):
        if choice not in InputOptions.MENU_CHOICES:
            raise NotValidInput('Input must be between (1-4)')
        return choice

class QuitProgram:
    def __init__(self):
        self.quit_program = False
        
    def set_quit(self, value):
        self.quit_program = value
        
    def should_quit(self):
        return self.quit_program
    
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