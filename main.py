def get_todos(filepath="files/todos.txt"):
    with open(filepath, 'r') as file_l:
        todos_l = file_l.readlines()
    return todos_l


def write_todos(todos_arg, filepath="files/todos.txt"):
    with open(filepath, 'w') as file_l:
        file_l.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete, clear or exit: ")
    user_action = user_action.strip() # remove trailing and leading spaces

    if user_action.startswith('add'):

        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):

        try:
            number = int(user_action[5:])

            number = number - 1; #index

            todos = get_todos()

            new_todo = input("Enter new todo for " + str(number+1) + ": ")
            todos[number] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Invalid command!")
            continue

    elif user_action.startswith('complete'):

        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"\"{todo_to_remove}\" completed!"
            print(message)

        except IndexError:
            print("No todo with that number!")
            continue
    
    elif user_action.startswith('clear'):

        write_todos([])

        message = "All todos cleared!"
        print(message)

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid action!")

print("Bye!")