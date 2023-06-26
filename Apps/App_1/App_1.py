# todos = []

while True:

    # Get user input and remove space
    usr_action = input('Type add, show, edit, complete, or exit: ')
    usr_action = usr_action.strip()

    match usr_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = []

            # for item in todos:
            #   new_item = item.strip('\n')
            #   new_todos.append(new_item)

            # List Comprehension
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                # index = index + 1
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input('Index of the todo to edit: '))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input('Enter a new todo: ')
            todos[number] = new_todo + '\n'
            # todos.pop(number)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input('Number of the todo to complete: '))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break
        case x:
            print('You entered an unknown command. Please enter a valid command!')

print('Bye!')

