while True:
    user_action = input("type add , show , edit , complete, exit: ")
    user_action = user_action.strip()

    if user_action.lower().startswith('add'):
        with open('files/todo.txt', 'r') as file:
            todos = file.readlines()
            todo = user_action[4:] + "\n"
            todos.append(todo)
        with open('files/todo.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.lower().startswith('show'):
        with open('files/todo.txt', 'r') as file:
            todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index+1}-{item}"
                print(row)

    elif user_action.lower().startswith('edit'):
        try:
            todo_number = int(user_action[5:])
            with open('files/todo.txt', 'r') as file:
                todos = file.readlines()
            print("Your Current todo: " + todos[todo_number])
            new_todo = input("Enter a new todo: ") + "\n"
            todos[todo_number-1] = new_todo
            with open('files/todo.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid Edit Command")
            continue
        except IndexError:
            print("Item not available in the todo list")

    elif user_action.lower().startswith('complete'):
        try:

            todo_complete = int(user_action[9:])
            with open('files/todo.txt', 'r') as file:
                todos = file.readlines()
                todos.pop(todo_complete - 1)
            with open('files/todo.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("No items at this number")
            continue
        except ValueError:
            print("Invalid Item number, Please type integer")
    else:
        print("Invalid option selected")
        break
print("Bye!")
