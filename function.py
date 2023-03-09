def read_todo(file_path="files/todo.txt"):
    with open(file_path, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todo(todo_args, file_path="files/todo.txt"):
    with open('files/todo.txt', 'w') as file:
        file.writelines(todo_args)
