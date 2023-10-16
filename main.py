while True:
    user_action = input("Type add, show, edit, complete, clear or exit: ")
    user_action = user_action.strip() # remove trailing and leading spaces

    if 'add' in user_action:
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif 'edit' in user_action:
        number = int(user_action[5:])

        number = number - 1; #index

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo for " + str(number+1) + ": ")
        todos[number] = new_todo + "\n"

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"\"{todo_to_remove}\" completed!"
        print(message)
    
    elif 'clear' in user_action:
        with open('files/todos.txt', 'w') as file:
            file.writelines([])
        
        message = "All todos cleared!"
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("Invalid action!")

print("Bye!")