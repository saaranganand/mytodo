def get_todos(filepath="files/todos.txt"):
    """Read the text file and return the list of to-do items."""

    with open(filepath, 'r') as file_l:
        todos_l = file_l.readlines()
    return todos_l


def write_todos(todos_arg, filepath="files/todos.txt"):
    """Write a list of to-do items to the text file."""

    with open(filepath, 'w') as file_l:
        file_l.writelines(todos_arg)

