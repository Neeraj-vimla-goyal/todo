FILEPATH = "files/todo.txt"


def read_todo(file_path=FILEPATH):
    """
    this function will read the text file and return the todo items list
    """
    with open(file_path, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todo(todo_args, file_path=FILEPATH):
    """
    this function will write todo items into text file
    """
    with open('files/todo.txt', 'w') as file:
        file.writelines(todo_args)
