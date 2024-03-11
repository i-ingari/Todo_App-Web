FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(to_do_list, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(to_do_list)


if __name__ == '__main__':
    print('Hello')
    print(get_todos())
