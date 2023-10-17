FILEPATH = "files/todos.txt"

def get_todos(filepath=FILEPATH):
    """Read the text file and return the list of to-do items."""

    with open(filepath, 'r') as file_l:
        todos_l = file_l.readlines()
    return todos_l


def write_todos(todos_arg, filepath=FILEPATH):
    """Write a list of to-do items to the text file."""

    with open(filepath, 'w') as file_l:
        file_l.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())