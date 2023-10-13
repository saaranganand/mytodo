while True:
    user_action = input("Type add, show, edit, complete, clear or exit: ")
    user_action = user_action.strip() # remove trailing and leading spaces

    match user_action:
        case 'add':
            todo = input("Enter your todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Enter todo number to edit: "))
            number = number - 1; #index

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Enter todo number to complete: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"{todo_to_remove} completed!"
            print(message)
        
        case 'clear':
            with open('files/todos.txt', 'w') as file:
                file.writelines([])
            
            message = "All todos cleared!"
            print(message)

        case 'exit':
            break

print("Bye!")