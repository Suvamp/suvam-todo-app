# from functions import get_todos, write_todos
import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)

while True:

    # Get user input and remove space
    usr_action = input('Type add, show, edit, complete, or exit: ')
    usr_action = usr_action.strip()

    if usr_action.startswith('add'):
        todo = usr_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)
    elif usr_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            # index = index + 1
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif usr_action.startswith('edit'):
        try:
            number = int(usr_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter a new todo: ')
            todos[number] = new_todo + '\n'
            # todos.pop(number)

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif usr_action.startswith('complete'):
        try:
            number = int(usr_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print('There is no item with that number.')
            continue

    elif usr_action.startswith('exit'):
        break

    else:
        print('Command is not valid')

    # if x:
        # print('You entered an unknown command. Please enter a valid command!')

# print('Bye!')
