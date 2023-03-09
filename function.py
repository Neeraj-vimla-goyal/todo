def read_todo():
    with open('files/todo.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local

