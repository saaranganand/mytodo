def get_todos(filepath):
    with open(filepath, 'r') as file_l:
        todos_l = file_l.readlines()
    return todos_l


while True:
    user_action = input("Type add, show, edit, complete, clear or exit: ")
    user_action = user_action.strip() # remove trailing and leading spaces

    if user_action.startswith('add'):

        todo = user_action[4:]

        todos = get_todos("files/todos.txt")

        todos.append(todo + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        todos = get_todos("files/todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):

        try:
            number = int(user_action[5:])

            number = number - 1; #index

            todos = get_todos("files/todos.txt")

            new_todo = input("Enter new todo for " + str(number+1) + ": ")
            todos[number] = new_todo + "\n"

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid command!")
            continue

    elif user_action.startswith('complete'):

        try:
            number = int(user_action[9:])

            todos = get_todos("files/todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"\"{todo_to_remove}\" completed!"
            print(message)
        except IndexError:
            print("No todo with that number!")
            continue
    
    elif user_action.startswith('clear'):

        with open('files/todos.txt', 'w') as file:
            file.writelines([])
        
        message = "All todos cleared!"
        print(message)

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid action!")

print("Bye!")