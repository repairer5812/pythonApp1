# todos =[]
import functions
import time

#
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        try:
            todos = functions.get_todos()

            # new_todos = []
            #
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            todos = [item.strip('\n') for item in todos]
            # print(todos)

            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index+1}-{item}"
                print(row)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()
            # print('Here is todos existing',todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            # print('Here is how it will be', todos)

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("you typed wrong one.")

print("Bye!")
