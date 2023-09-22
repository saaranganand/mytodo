todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip() # remove trailing and leading spaces

    match user_action:
        case 'add':
            todo = input("Enter your todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Enter todo number to edit: "))
            number = number - 1; #index
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break

print("Bye!")