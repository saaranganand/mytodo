todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip() # remove trailing and leading spaces

    match user_action:
        case 'add':
            todo = input("Enter your todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter todo number to edit: "))
            number = number; #index
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Enter todo number to complete: "))
            todos.pop(number-1)
        case 'exit':
            break

print("Bye!")