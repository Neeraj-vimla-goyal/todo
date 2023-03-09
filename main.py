from function import read_todo, write_todo
while True:
    user_action = input("type add , show , edit , complete, exit: ")
    user_action = user_action.strip()

    if user_action.lower().startswith('add'):
        todos = read_todo()
        todo = user_action[4:] + "\n"
        todos.append(todo)
        write_todo(todo_args=todos)

    elif user_action.lower().startswith('show'):
        todos = read_todo()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.lower().startswith('edit'):
        try:
            todo_number = int(user_action[5:])
            todos = read_todo()
            print("Your Current todo: " + todos[todo_number - 1])
            new_todo = input("Enter a new todo: ") + "\n"
            todos[todo_number-1] = new_todo
            write_todo(todo_args=todos)
        except ValueError:
            print("Invalid Edit Command")
            continue
        except IndexError:
            print("Item not available in the todo list")

    elif user_action.lower().startswith('complete'):
        try:

            todo_complete = int(user_action[9:])
            todos = read_todo()
            print("todo: " + todos[todo_complete - 1].strip()+ " is completed")
            todos.pop(todo_complete - 1)
            write_todo(todo_args=todos)
        except IndexError:
            print("No items at this number")
            continue
        except ValueError:
            print("Invalid Item number, Please type integer")
    else:
        print("Invalid option selected")
        break
print("Bye!")
